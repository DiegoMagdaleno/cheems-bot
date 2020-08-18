from dataclasses import dataclass
import requests
import datetime

from requests.api import request


class NoArticlesOrNotFound(Exception):
    pass


@dataclass
class WikipediaArticle:
    name: str
    description: str
    last_modified: str
    url: str
    author: str = "Wikipedia"
    icon_url: str = "https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png"


class Wikipedia:
    def __init__(self, query) -> None:
        self.query = query

        self.search = requests.get(
            (
                "https://en.wikipedia.org//w/api.php?action=query"
                "&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop="
            ).format(self.query)
        ).json()["query"]

        if self.search["searchinfo"]["totalhits"] == 0:
            raise NoArticlesOrNotFound
        for each_search in range(len(self.search["search"])):
            self.article = self.search["search"][each_search]["title"]
            self.request = requests.get(
                (
                    "https://en.wikipedia.org//w/api.php?action=query"
                    "&utf8=1&redirects&format=json&prop=info|images"
                    "&inprop=url&titles={}"
                ).format(self.article)
            ).json()["query"]["pages"]
            if str(list(self.request)[0]) != "-1":
                break
            else:
                raise NoArticlesOrNotFound

        self.request_properties = self.request[list(self.request)[0]]

        self.article = self.request_properties["title"]
        self.article_url = self.request_properties["fullurl"]
        self.article_description = requests.get(
            "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(self.article)
        ).json()["extract"]

        self.last_edit = datetime.datetime.strptime(
            self.request_properties["touched"], "%Y-%m-%dT%H:%M:%SZ"
        )

    def get_wikipedia_article(self) -> WikipediaArticle:
        self.our_article = WikipediaArticle(
            self.article, self.article_description, self.last_edit, self.article_url
        )
        return self.our_article
