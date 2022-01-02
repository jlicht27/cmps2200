from collections import defaultdict
from heapq import heappush, heappop
from math import sqrt

def prim(graph):
    """
    ### TODO:
    Update this method to work when the graph has multiple connected components.
    Rather than returning a single tree, return a list of trees,
    one per component, containing the MST for each component.

    Each tree is a set of (weight, node1, node2) tuples.
    """

    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)
            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)
                # record this edge in the tree
                tree.add((weight, node, parent))
                visited.add(node)
                for neighbor, w in graph[node]:
                    heappush(frontier, (w, neighbor, node))
                    # compare with dijkstra:
                    # heappush(frontier, (distance + weight, neighbor))

                return prim_helper(visited, frontier, tree)

    def element_remover(graph, tree):
        # get tree elements
        tree_elements = []
        for i in tree:
            tree_elements.append(i[1])

        # retrieve nodes that have already been visited
        elements_to_remove = []
        for j in graph.keys():
            if j in tree_elements:
                elements_to_remove.append(j)

        # remove those elements
        for k in elements_to_remove:
            graph.pop(k)
        return graph

    result = []
    while len(graph) > 0:
        # pick first node as source arbitrarily
        source = list(graph.keys())[0]
        frontier = []
        heappush(frontier, (0, source, source))
        visited = set()  # store the visited nodes (don't need distance anymore)
        tree = set()
        result.append(prim_helper(visited, frontier, tree))
        graph = element_remover(graph, tree)

    if len(result) == 1:  # if just a single element just don't return it as a list
        return result[0]
    else:
        return result


def test_prim():
    graph = {
        's': {('a', 4), ('b', 8)},
        'a': {('s', 4), ('b', 2), ('c', 5)},
        'b': {('s', 8), ('a', 2), ('c', 3)},
        'c': {('a', 5), ('b', 3), ('d', 3)},
        'd': {('c', 3)},
        'e': {('f', 10)},  # e and f are in a separate component.
        'f': {('e', 10)}
    }

    trees = prim(graph)
    assert len(trees) == 2
    # since we are not guaranteed to get the same order
    # of edges in the answer, we'll check the size and
    # weight of each tree.
    len1 = len(trees[0])
    len2 = len(trees[1])
    assert min([len1, len2]) == 2
    assert max([len1, len2]) == 5

    sum1 = sum(e[0] for e in trees[0])
    sum2 = sum(e[0] for e in trees[1])
    assert min([sum1, sum2]) == 10
    assert max([sum1, sum2]) == 12
    ###


def mst_from_points(points):
    """
    Return the minimum spanning tree for a list of points, using euclidean distance
    as the edge weight between each pair of points.
    See test_mst_from_points.

    Params:
    points... a list of tuples (city_name, x-coord, y-coord)

    Returns:
    a list of edges of the form (weight, node1, node2) indicating the minimum spanning
    tree connecting the cities in the input.
    """
    graph = {}
    for i in range(len(points)):
        s = set()
        for j in range(len(points)):
            if i is not j:
                distance = euclidean_distance(points[i], points[j])
                s.add((points[j][0], distance))
        graph[points[i][0]] = s
    return prim(graph)


def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83


def test_mst_from_points():
    points = [('a', 5, 10),  # (city_name, x-coord, y-coord)
              ('b', 7, 12),
              ('c', 2, 3),
              ('d', 12, 3),
              ('e', 4, 6),
              ('f', 6, 7)]
    tree = mst_from_points(points)
    # check that the weight of the MST is correct.
    assert round(sum(e[0] for e in tree), 2) == 19.04
