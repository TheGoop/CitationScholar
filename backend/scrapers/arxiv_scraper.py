import graphlib
import feedparser
import urllib.parse

from backend.scrapers.interface.scraper import Scraper

class ArxivScraper(Scraper):
    def __init__(self):
        super().__init__('arxiv')

    def findPaper(self, citation):
        url = ('http://export.arxiv.org/api/query?'
                + 'search_query='
                + urllib.parse.quote(citation.get_title())
                + '&start=0&max_results=10')
        papers = feedparser.parse(url).entries

        for paper in papers:
            if not hasattr(paper, 'links'):
                continue
            for link in paper.links:
                if link.type == 'application/pdf':
                    link_text = link.href
                    if link_text[-4] != ".pdf":
                        link_text += ".pdf"
                    return link_text

        return None


if __name__ == '__main__':
    class Mock:
        def get_title(self):
            return 'Communicating Sequential Processes'
    print(ArxivScraper().findPaper(Mock()))
