class PaperNode:
    def __init__(self, citation, pdf_hash):
        if not citation or not pdf_hash:
            return ValueError("Citation and pdf_hash must not be empty")
        self.citation = citation
        self.pdf_hash = pdf_hash

    def __hash__(self):
        return self.pdf_hash

    def __eq__(self, other):
        if isinstance(other, PaperNode):
            return self.pdf_hash == other.pdf_hash
        return NotImplemented
