from pdfminer import high_level
import uuid
import requests

class PDF():

    def _construct_file_name(self):
        #make a random UUID that will be the name of the file based on the host ID and current time
        name = str(uuid.uuid1())
        return 'pdfs/' + name + ".pdf"

    def _scrape_pdf(self):
        #make a random UUID that will be the name of the file based on the host ID and current time
        filename = self._construct_file_name()
        try:
            r = requests.get(self.url, stream=True)
        except:
            raise ValueError

        chunk_size = 2000
        try:
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
        except:
            raise IOError
        
        return filename

    def _load_pdf(self):
        if not self.url:
            raise ValueError

        filename = self._scrape_pdf()
        with open(filename, 'rb') as fd:
            self.pdf_hash = hash(fd.read())

        extracted_text = high_level.extract_text(filename, "")
        self.text = extracted_text

    def __init__(self, link):
        self.url = link
        self.text = None
        self.pdf_hash = None
        self._load_pdf()

    def get_text(self):
        return self.text
    
    def get_hash(self):
        return self.pdf_hash

    def get_url(self):
        return self.url
    



if __name__ == "__main__":
    path = '/Users/akshay/projects/helloworld/LAHacks21/test.pdf'
    path = 'https://arxiv.org/pdf/2103.13916.pdf'
    x = PDF(path)
    print(x.get_text())
    print(x.get_hash())