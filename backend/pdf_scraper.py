import PyPDF2


class PDF():

    def _pdf_to_text(pdf):
        raise NotImplementedError

    def _get_pdf():
        raise NotImplementedError

    def _scrape_link():
        if not self.link:
            raise ValueError

    def __init__(self, link):
        self.link = link
        self.text = None
        self.pages = None
        self._scrape_link()

    def get_text(self):
        return self.text

    def get_num_pages(self):
        return self.pages
