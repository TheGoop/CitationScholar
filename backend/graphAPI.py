from backend.finder import Finder
from backend.citation
def createDependencyGraph(body):
    scrapers = []
    for key in body:
        if key == 'input':
            continue
        scrapers.append(key)
    link = body['input']
    try:



