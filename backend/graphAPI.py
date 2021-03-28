from backend.finder import Finder
from backend.citation_scraper import CitationExtractor
from backend.PaperNode import PaperNode
from backend.CitationAlgorithm import create_dependency_graph
def createDependencyGraph(body):
    scrapers = []
    for key in body:
        if key == 'input':
            continue
        scrapers.append(key)
    link = body['input']
    try:
        finder = Finder(scrapers)
    except ValueError:
        return None, 1
    try:
        extractor = CitationExtractor(link)
        initial_references, pdf_hash = extractor.extract_citations()
    except ValueError:
        return None, 2
    except NotImplementedError:
        return None, 3
    except ConnectionError:
        return None, 4
    root_node = PaperNode(link, pdf_hash)
    try:
        citation_ordered_list, graph = create_dependency_graph(root_node, initial_references, finder)
    except ValueError:
        return None, 5
    payload = {}
    payload['ordered_list'] = _extract_citations_from_node_list(citation_ordered_list)
    payload['graph'] = _extract_citations_from_graph(graph)
    return payload, 0

def _extract_citations_from_node_list(node_list):
    return [node.citation for node in node_list]

def _extract_citations_from_graph(graph):
    citation_graph = {}
    for key in graph:
        citation_graph[key.citation] = set()
        for item in graph[key]:
            citation_graph[key.citation].add(item.citation)
    return citation_graph





