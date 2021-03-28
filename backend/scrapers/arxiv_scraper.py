import graphlib
import feedparser

from backend.scrapers.interface.scraper import Scraper

class ArxivScraper(Scraper):
    def __init__(self):
        super().__init__('arxiv')

    def findPaper(self, citation):
        url = ('http://export.arxiv.org/api/query?'
                + f'search_query={citation}'
                + '&start=0&max_results=10')
        papers = feedparser.parse(url).entries

        for paper in papers:
            if not hasattr(paper, 'links'):
                continue
            for link in paper.links:
                if link.type == 'application/pdf':
                    return link.href

        return None


if __name__ == '__main__':
    print(ArxivScraper().findPaper('Electron'))
