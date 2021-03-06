from backend.scrapers import *
from backend.scrapers.arxiv_scraper import ArxivScraper

class Finder():
    def __init__(self, scrapers):
        # Add more scrapers to this map as they are implemented.
        keyword_map = { 'arxiv': ArxivScraper }

        self.scrapers = []
        for scraper in scrapers:
            if scraper not in keyword_map:
                raise ValueError(f"'{scraper}' is not a supported scraper.")
            self.scrapers.append(keyword_map[scraper]())

    def findPaper(self, citation):
        """Given a citation, return a PDF link to its corresponding paper.

        For now, `citation` is a keyword that arXiv can search by. In the
        future, we will make this a more specific object.
        """

        for scraper in self.scrapers:
            res = scraper.findPaper(citation)
            if res is not None:
                return res
        return None
