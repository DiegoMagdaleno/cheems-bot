from dataclasses import dataclass
import requests
from loguru import logger as log


class GitHubRepositoryError(Exception):
    pass


@dataclass
class GitHubRepository:
    name: str
    full_name: str
    is_private: bool
    owner: str
    description: str
    forks: str
    open_issues: str
    watchers: str


class GitHub:
    def __init__(self, repository) -> None:
        self.repository = repository

        try:
            self.repository_request = requests.get(
                f"https://api.github.com/repos/{self.repository}"
            )
            self.repository_request.raise_for_status()
        except Exception as e:
            log.warning(f"Had an trying to load user desired repository {e}")
            raise GitHubRepositoryError

    def get_github_repo(self):
        self.json_response = self.repository_request.json()
        self.githubrepo = GitHubRepository(
            self.json_response["name"],
            self.json_response["full_name"],
            self.json_response["private"],
            self.json_response["owner"]["login"],
            self.json_response["description"],
            self.json_response["forks"],
            self.json_response["open_issues"],
            self.json_response["watchers"],
        )
        return self.githubrepo
