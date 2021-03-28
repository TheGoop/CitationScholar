from backend.finder import Finder
from backend.citation_scraper import CitationExtractor
from backend.PaperNode import PaperNode
from backend.CitationAlgorithm import create_dependency_graph

def createDependencyGraph(body):
    scrapers = []
    for key in body['valid']:
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
    root_node = PaperNode("Queried Paper", link, pdf_hash)
    try:
        citation_ordered_list, graph = create_dependency_graph(root_node, initial_references, finder)
    except ValueError:
        return None, 5
    payload = {}
    payload['nodes'] = _extract_node_info_from_node_list(citation_ordered_list)
    payload['edges'] = _extract_edges_from_graph(graph)
    payload['ordered'] = _extract_titles_from_node_list(citation_ordered_list)
    return payload, 0

def _extract_node_info_from_node_list(node_list):
    return [{"id": node.id, "link": node.link} for node in node_list]

def _extract_edges_from_graph(graph):
    return [{"source": parent.id, "target": child.id} for parent in graph for child in graph[parent]]

def _extract_titles_from_node_list(node_list):
    return [node.id for node in node_list]




