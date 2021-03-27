import graphlib
import feedparser

from scraper import Scraper

class ArxivScraper(Scraper):
    def __init__(self):
        super().__init__('arxiv')

    def findPaper(self, citation):
        url = ('http://export.arxiv.org/api/query?'
                + f'search_query={citation}'
                + '&start=0&max_results=1')
        results = feedparser.parse(url).entries

        if len(results) == 0:
            return None

        return results[0]


if __name__ == '__main__':
    print(ArxivScraper().findPaper('dijkstra'))
