from backend.pdf_scraper import PDF
import requests, json


class Author:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


class Citation:
    def _load_authors(self, authors):
        self.authors = []
        for a in authors:
            t = Author(a["name"], a["authorId"])
            self.authors.append(t)
        #pass
        #raise NotImplementedError

    def __init__(self, title, authors, doi, year, paper_id, arxiv_id):
        self.title = title
        self.authors = None
        self.doi = doi
        self.year = year
        self.paper_id = paper_id
        self.arxiv_id = arxiv_id
        self._load_authors(authors)

    def get_title(self):
        return self.title

    def get_authors(self):
        return self.authors

    def get_doi(self):
        return self.doi

    def get_year(self):
        return self.year

    def get_paper_id(self):
        return self.paper_id

    def get_arxiv_id(self):
        return self.arxiv_id

    def get_url(self):
        return "https://www.semanticscholar.org/paper/" + self.paper_id

    def __repr__(self):
        return str((self.get_title(), self.get_paper_id()))


class CitationExtractor:
    def _extract_id(self):
        s = "/pdf/"
        i = self.url.find(s)
        self.id = self.url[i + len(s):-4]
        return self.id

    def __init__(self, arxiv_url):
        if not isinstance(arxiv_url, str) or len(arxiv_url) <= 4 or arxiv_url[
                -4:] != ".pdf" or "/pdf/" not in arxiv_url:
            raise ValueError
        if "arxiv" not in arxiv_url:
            raise NotImplementedError

        self.url = arxiv_url
        self.id = None
        self.raw_citations = None
        self.citations = None
        try:
            self._extract_id()
        except:
            raise ValueError
        self._load_raw_citations()
        self._load_citations()

        self.pdf = PDF(self.url)

    def _make_request_url(self):
        url = "https://api.semanticscholar.org/v1/paper/arXiv:" + self.id
        return url

    def _load_raw_citations(self):
        request_url = self._make_request_url()
        try:
            r = requests.get(request_url)
            d = r.json()
            self.raw_citations = d["citations"] + d["references"]
        except:
            raise ConnectionError

    def get_raw_citations(self):
        return self.raw_citations

    def _load_citations(self):
        if not self.raw_citations:
            self.citations = None
        self.citations = []
        for cite in self.raw_citations:
            t = Citation(cite['title'], cite['authors'], cite['doi'],
                         cite['year'], cite['paperId'], cite['arxivId'])
            self.citations.append(t)

    def get_citations(self):
        return self.citations

    def get_hash(self):
        return self.pdf.get_hash()

    def extract_citations(self):
        return (self.get_citations(), self.get_hash())


if __name__ == "__main__":
    x = CitationExtractor("https://arxiv.org/pdf/1705.10311.pdf")
    #print(x.get_raw_citations()[0])
    [print(i) for i in x.get_citations()]
