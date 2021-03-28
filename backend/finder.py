from scrapers import *

class Finder():
    def __init__(self, scrapers):
        # Add more scrapers to this map as they are implemented.
        keyword_map = { 'arxiv': ArxivScraper }

        self.scrapers = []
        for scraper in scrapers:
            if scraper not in keyword_map:
                raise ValueError(f"'{scraper}' is not a supported scraper.")
            self.scrapers.append(keyword_map[scraper]())

    def findPaper(citation):
        for scraper in self.scrapers:
            res = scraper.findPaper(citation)
            if res is not None:
                return res
        return None
