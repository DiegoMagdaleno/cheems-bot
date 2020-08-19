import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from dataclasses import dataclass


@dataclass
class DuckDuckGoResult:
    title: str
    quick_snippet: str
    url: str

class DuckDuckGoHandler():
    def __init__(self, query:str):
        self.query = query
        self.results_info_snippet = []
        self.links_pre = []
        self.objects_list_duck = []
    
        self.duckduckgo_site = urllib.request.urlopen('https://duckduckgo.com/html/?q={}'.format(self.query))
        self.data = self.duckduckgo_site.read()

        # Here is where the magic starts
        self.parsed = BeautifulSoup(self.data, "html.parser")

        self.results_quick_links = self.parsed.find_all("div", {"id":"links"})[0]

        self.results_title = self.results_quick_links.find_all('h2', attrs={'class':'result__title'})

        self.results_info = self.results_quick_links.find_all('a', attrs={'class':'result__snippet'})

        self.raw_html_title = BeautifulSoup(str(self.results_title), "html.parser").text
        
        # Lets clean our HTML so we can get our titles
        self.array_of_titles = (((str(self.raw_html_title).replace("[", "")).replace("]", "")).strip()).split(",")
        for iteration, title in enumerate(self.array_of_titles):
            self.array_of_titles[iteration] = title.strip()
        
        # Now lets grab the short text

        for iteration, quick_snippet in enumerate(self.results_info):
            self.results_info_snippet.append(BeautifulSoup(str(quick_snippet), "html.parser").find().text)

        # Lets grab our links
        for result in self.results_info:
            self.url = result['href']
            self.o = urllib.parse.urlparse(self.url)
            self.d = urllib.parse.parse_qs(self.o.query)
            self.links_pre.append(self.d['uddg'][0])

        # At this point we have all, titles, short text and our links. 
        # Now its time to make our arrays smaller, and parse all this into an object!

        self.titles = self.array_of_titles[:5]
        self.snippets = self.results_info_snippet[:5]
        self.links = self.links_pre[:5]

        # At this point I am questioning my life decisions I was supposed to 
        # spend 30 minutes on this and I have been working 2 hours on this 
        # im in constant pain thanks to do this, never doing web scrapping again

        # Anyway next step:

        # Parse them into an object, so lets init them

    def get_results(self):
        for title in self.titles:
            for snippet in self.snippets:
                for link in self.links:
                    self.objects_list_duck.append(DuckDuckGoResult(title, snippet, link))
        return self.objects_list_duck