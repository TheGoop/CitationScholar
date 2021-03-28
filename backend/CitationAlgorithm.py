import queue
from graphlib import TopologicalSorter
from backend.PaperNode import PaperNode
from backend.citation_scraper import CitationExtractor

def create_dependency_graph(root_node, citations, finder):
    graph = {root_node: set()}
    citation_stack = queue.Queue()
    for citation in _append_parent_to_citations(root_node, citations):
        citation_stack.put(citation)
    max_iters = 100
    curr_iter = 1
    while not citation_stack.empty() and curr_iter <= max_iters:
        curr_citation, curr_parent = citation_stack.get()
        if curr_parent not in graph:
            raise ValueError(f'Current Parent {curr_parent} not found in graph')

        citation_link = finder.findPaper(curr_citation)
        if citation_link is None:
            continue
        try:
            extractor = CitationExtractor(citation_link)
            reference_list, pdf_hash = extractor.extract_citation()
        except ValueError:
            continue
        except NotImplementedError:
            continue
        except ConnectionError:
            continue

        curr_node = PaperNode(curr_citation.get_title(), citation_link, curr_citation.get_year(), pdf_hash)
        for citation in _append_parent_to_citations(curr_node, reference_list):
            citation_stack.put(citation)

        graph[curr_parent].add(curr_node)
        graph[curr_node] = set()
        curr_iter += 1

    sorter = TopologicalSorter(graph)
    topo_order = sorter.static_order()
    return topo_order, graph



def _append_parent_to_citations(parent, citations):
    return [(citation, parent) for citation in citations]

# if __name__ == "__main__":
    # class DummyFinder:
    #     def findPaper(self, citation):
    #         return 'link:' + str(citation)
    #
    # class DummyExtractor:
    #     citation_map = {1: [2,5], 2: [3,4], 3: [], 4: [], 5: [4,6], 6: [7], 7: [4]}
    #     def extract_citation(self, link):
    #         paperNum = int(link[-1])
    #         return self.citation_map[paperNum], hash(paperNum)
    #
    # root_node = PaperNode(1, hash(1))
    # citations = [2, 5]
    # finder = DummyFinder()
    # extractor = DummyExtractor()
    # ordered_list, graph = create_dependency_graph(root_node, citations, finder, extractor)
    # print(ordered_list)
    # display_graph = {}
    # for key in graph:
    #     display_graph[key.citation] = set()
    #     for item in graph[key]:
    #         display_graph[key.citation].add(item.citation)
    # print(display_graph)
