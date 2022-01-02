from collections import defaultdict


def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = {start_node}
    frontier = {start_node}
    while len(frontier) != 0:
        node = frontier.pop()
        result.add(node)
        friends = graph[node]
        for i in friends:
            if i not in result:
                frontier.add(i)

    return result


def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    print(graph)
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']


def list_creator(graph):
    graph_list = []
    for i in graph.keys():
        graph_list.append(i)
    return graph_list


def connected(graph):
    graph_list = list_creator(graph)
    if sorted(reachable(graph, graph_list[0])) == sorted(graph_list):
        return True
    else:
        return False


def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    graph_list = list_creator(graph)
    counter = 0
    while len(graph_list) > 0:
        counter += 1
        result = reachable(graph, graph_list[0])
        for i in result:
            graph_list.remove(i)

    return counter


def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
