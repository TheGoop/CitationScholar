#from refextract import extract_references_from_file
from PyPDF2 import PdfFileReader

from pdfminer import high_level


class PDF():
    def _scrape_pdf(self):
        if not self.link:
            raise ValueError

        pdf_file_obj = open(self.link, 'rb')

        extracted_text = high_level.extract_text(self.link, "")
        self.text = extracted_text

    def __init__(self, link):
        self.link = link
        self.text = None
        self._scrape_pdf()

    def get_text(self):
        return self.text


if __name__ == "__main__":
    path = '/Users/akshay/projects/helloworld/LAHacks21/test.pdf'
    x = PDF(path)
    print(x.get_text())