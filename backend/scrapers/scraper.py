# All Scrapers should implement this interface.
# To add a new scraper, just plonk it in this directory.

from abc import ABC, abstractmethod

class Scraper(ABC):
    """This class defines the interface that all Scrapers must implement."""
    def __init__(self, name):
        self.name = name

    def getName():
        return self.name

    @abstractmethod
    def findPaper(citation):
        pass
