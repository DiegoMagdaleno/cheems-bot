from dataclasses import dataclass
from google_images_search import GoogleImagesSearch
from loguru import logger as log


@dataclass
class GoogleCredentials:
    api_key: str
    cx: str

class NoResults(Exception):
    pass

class GoogleSession:
    def __init__(self, api_key, cx) -> None:
        self.api_key = api_key
        self.cx = cx

        self.google_session = GoogleImagesSearch(
            developer_key=self.api_key, custom_search_cx=self.cx
        )

        self.link_list = []


class GoogleImageSearch(GoogleSession):
    def __init__(self, google_credentials: GoogleCredentials, search_term: str, safe_search: str) -> None:
        self.google_credentials = google_credentials
        super().__init__(self.google_credentials.api_key, self.google_credentials.cx)
        self.search_term = search_term
        self.safe_search = safe_search

        _search_params = {
            "q": self.search_term,
            "num": 10,
            "safe": self.safe_search,
        }

        self.google_session.search(search_params=_search_params)
        if len(self.google_session.results()) <= 0:
            log.warning("Nothing found for this query. Raising exception.")
            raise NoResults


        for image in self.google_session.results():
            log.info(f"Appending {image} to image results list")
            self.link_list.append(image.url)
        