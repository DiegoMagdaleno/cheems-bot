from typing import Mapping
from pymongo.errors import PyMongoError

class IdNotFound(PyMongoError):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message

class DocumentExecutor:
    def __init__(self, db) -> None:
        self.db = db
    
    async def find_by_id(self, _id):
        data = await self.db.find_one({"_id": _id})

        if not data:
            raise IdNotFound()

        return data

    async def find_by_custom(self, filter):
        if not isinstance(filter, Mapping):
            raise TypeError(f"Expected Dictionary got: {type(filter)}")

        data = await self.db.find_one(filter)
        if not data:
            raise IdNotFound()
        return data

    async def delete_by_id(self, _id):
        await self.find_by_id(_id)

        await self.db.delete_many({"_id": _id})
    
    async def insert(self, dict: Mapping):
        if not isinstance(dict, Mapping):
            raise TypeError(f"Expected Dictionary got: {type(dict)}")
        
        if not dict["_id"]:
            raise KeyError("_id was not supplied in the dictionary")
            
        await self.db.insert_one(dict)

    async def upsert(self, data, option="set", *args, **kwargs):
        await self.update_by_id(data, option, upsert=True, *args, **kwargs)

    async def update_by_id(self, data, option="set", *args, **kwargs):
        upsert = kwargs.get("upsert", False)

        if not isinstance(data, Mapping):
            raise TypeError(f"Expected Dictionary got {type(data)}")

        if not data.get("_id"):
            raise KeyError("_id not found in supplied dict.")

        try:
            await self.find_by_id(data["_id"])
        except IdNotFound as e:
            if not upsert:
                raise e

        _id = data["_id"]
        data.pop("_id")
        await self.db.update_one({"_id": _id}, {f"${option}": data}, *args, **kwargs)
    
    async def unset(self, dict):
        if not isinstance(dict, Mapping):
            raise TypeError(f"Expected Dictionary got: {type(dict)}")
    
        if not dict["_id"]:
            raise KeyError("_id was not supplied in the dictionary")   
            
        if not await self.find_by_id(dict["_id"]):
            return
        
        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$unset": dict})

    async def increment(self, id, amount, field):
        if not await self.find_by_id(id):
            pass
        
        self.db.update_one({"_id": id}, {"$inc", {field: amount}})
    
        

class DocumentInteractor(DocumentExecutor):
    def __init__(self, connection, document_name) -> None:
        self.db = connection[document_name]
        super().__init__(self.db)

    async def update(self, target_dict, *args, **kwargs):
        await self.update_by_id(target_dict, *args, **kwargs)
    
    async def get_all(self, filter={}, *args, **kwargs):
        return await self.db.find(filter, *args, **kwargs).to_list(None)

    async def get_by_id(self, id):
        return await self.find_by_id(id)
    
    async def find(self, _id):
        return await self.find_by_id(_id)
    
    async def delete(self, _id):
        await self.delete_by_id(_id)
    