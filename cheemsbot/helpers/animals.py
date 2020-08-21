import requests
import nekos

from loguru import logger as log


class Animals:
    def shiba(self) -> str:
        try:
            self.api_response = requests.get(
                "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
            )
            self.api_response.raise_for_status()
        except requests.exceptions.HTTPError:
            log.exception("Fatal! HTTP Error")
            return
        except requests.exceptions.ConnectionError:
            log.exception("Connection error!")
            return
        except requests.exceptions.Timeout:
            log.exception("The API returned a timeout")
            return
        except requests.exceptions.RequestException:
            log.exception("Some other critical error happened")
            return
        log.debug(
            f"Got API response from shivas.online sending the following image url {self.api_response.json()[0]}"
        )
        return self.api_response.json()[0]

    def cat(self) -> str:
        try:
            self.cat_image_url = nekos.cat()
        except nekos.errors.NothingFound:
            log.exception("Nothing found on Nekos.py for this cat request")
            return
        except nekos.errors.EmptyArgument:
            log.exception("Empty argument")
            return
        except nekos.errors.InvalidArgument:
            log.exception("Invalid argument for nekos.py")
            return
        except nekos.errors.NekoException:
            log.exception("Some other error ocurred on Nekos.py execution.")
            return
        log.debug(
            f"Got image API response from Nekos.py on cat, sending the following image url {str(self.cat_image_url)}"
        )
        return str(self.cat_image_url)

    def dog(self) -> str:
        try:
            self.dog_image_url = nekos.img("woof")
        except nekos.errors.NothingFound:
            log.exception("Nothing found on Nekos.py for this dog request")
            return
        except nekos.errors.EmptyArgument:
            log.exception("Empty argument")
            return
        except nekos.errors.InvalidArgument:
            log.exception("Invalid argument for nekos.py")
            return
        except nekos.errors.NekoException:
            log.exception("Some other error ocurred on Nekos.py execution.")
            return
        log.debug(
            f"Got image API response from Nekos.py on dog, sending the following image url {str(self.dog_image_url)}"
        )
        return self.dog_image_url

    def fox(self) -> str:
        try:
            self.fox_img_url = requests.get("https://randomfox.ca/floof/")
            self.fox_img_url.raise_for_status()
        except requests.exceptions.HTTPError:
            log.exception("Fatal! HTTP Error")
            return
        except requests.exceptions.ConnectionError:
            log.exception("Connection error!")
            return
        except requests.exceptions.Timeout:
            log.exception("The API returned a timeout")
            return
        except requests.exceptions.RequestException:
            log.exception("Some other critical error happened")
            return
        log.debug(
            f"Got API response from randomfox.ca sending the following image url {self.fox_img_url.json()['image']}"
        )

        return self.fox_img_url.json()["image"]
