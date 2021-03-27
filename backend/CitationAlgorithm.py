def create_dependency_graph(root_node, citations):
    nodes = {}
    nodes.add(root_node)
    citation_stack = _append_parent_to_citations(root_node, citations)

def _append_parent_to_citations(parent, citations):
    return [(citation, parent) for citation in citations]