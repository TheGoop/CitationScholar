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
    root_node = PaperNode("Queried Paper", link, 2021, pdf_hash)
    try:
        citation_ordered_list, graph = create_dependency_graph(root_node, initial_references, finder)
    except ValueError:
        return None, 5
    payload = {}
    payload['nodes'], payload['ordered'] = _extract_node_info_from_node_list(citation_ordered_list)
    payload['edges'] = _extract_edges_from_graph(graph)
    return payload, 0

def _extract_node_info_from_node_list(node_list):
    nodes = []
    ordered = []
    for node in node_list:
        nodes.append({"id": node.id, "link": node.link, "year": node.year})
        ordered.append(node.id)
    return nodes, ordered

def _extract_edges_from_graph(graph):
    return [{"source": parent.id, "target": child.id} for parent in graph for child in graph[parent]]




