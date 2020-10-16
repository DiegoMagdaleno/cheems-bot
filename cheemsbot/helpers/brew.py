from dataclasses import dataclass
from typing import List
import requests

class NoHomebrewFormuale(Exception):
    pass



@dataclass
class HomebrewPackage:
    name: str
    desc: str
    homepage: str
    version: str
    dependencies: List[str]


class HomebrewInteracter:
    def __init__(self, target_formula) -> None:
        self.target_formula = target_formula

    def get_target_formula(self) -> HomebrewPackage:
        self.json_response = requests.get(
            f"https://formulae.brew.sh/api/formula/{self.target_formula}.json"
        )
        if self.json_response.status_code == 404:
            raise NoHomebrewFormuale
        self.json_response = self.json_response.json()
        self.homebrew_package_meta = HomebrewPackage(
            name=self.json_response["name"],
            desc=self.json_response["desc"],
            version=self.json_response["versions"]["stable"],
            dependencies=self.json_response["dependencies"],
            homepage=self.json_response["homepage"],
        )
        return self.homebrew_package_meta
