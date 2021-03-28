class PaperNode:
    def __init__(self, id, link, year, pdf_hash):
        if not id or not link or not pdf_hash or not year:
            return ValueError("Citation and pdf_hash must not be empty")
        self.id = id
        self.link = link
        self.year = year
        self.pdf_hash = pdf_hash

    def __hash__(self):
        return self.pdf_hash

    def __eq__(self, other):
        if isinstance(other, PaperNode):
            return self.pdf_hash == other.pdf_hash
        return NotImplemented
