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
    
    async def find_by_id(self, id):
        return await self.db.find_one({"_id": id})
    
    async def delete_by_id(self, id):
        if not await self.find_by_id():
            pass
        
        await self.db.delete_many({"_id": id})
    
    async def insert(self, dict: Mapping):
        if not isinstance(dict, Mapping):
            raise TypeError(f"Expected Dictionary got: {type(dict)}")
        
        if not dict["_id"]:
            raise KeyError("_id was not supplied in the dictionary")
            
        await self.db.insert_one(dict)

    async def upsert(self, dict):
        if await self.__get_raw(dict["_id"]) is not None:
            await self.update_by_id(dict)
        else:
            await self.db.insert_one(dict)
    
    async def update_by_id(self, dict):
        if not isinstance(dict, Mapping):
            raise TypeError(f"Expected Dictionary got: {type(dict)}")

        if not dict["_id"]:
            raise KeyError("_id was not supplied in the dictionary")
    
        if not await self.find_by_id(dict["id"]):
            pass
            
        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$set": dict})
    
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
    
    async def get_all(self):
        data = []
        async for document in self.db.find({}):
            data.append(document)
        return data
    
    async def __get_raw(self, id):
        return await self.db.find_one({"_id": id})
    


class DocumentInteractor(DocumentExecutor):
    def __init__(self, connection, document_name) -> None:
        self.db = connection[document_name]
        super().__init__(self.db)

    async def update(self, target_dict):
        await self.update_by_id(target_dict)
    
    async def get_by_id(self, id):
        return await self.find_by_id(id)
    
    async def find(self, id):
        return await self.find_by_id(id)
    
    async def delete(self, id):
        await self.delete_by_id(id)
    