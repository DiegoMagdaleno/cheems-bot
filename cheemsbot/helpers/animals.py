import requests
import nekos

class Animals:
    def shiba(self):
        self.api_response = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true").json()
        return self.api_response[0]

    def cat(self):
        self.cat_image_url = str(nekos.cat())
        return self.cat_image_url
    
    def dog(self):
        self.dog_image_url = str(nekos.img('woof'))
        return self.dog_image_url
