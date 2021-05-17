from dijkstra import dijkstra
import copy

def _add_shortcut(graph, node):
    '''add the shortcuts instead of a node '''
    for backward_neighbour in _get_backward_neighbours(graph, node):
       for front_neighbour in graph[node]:
               distance, predecessor = dijkstra(graph, backward_neighbour, front_neighbour)
               if predecessor is node:
                   _addEdge(graph, backward_neighbour, front_neighbour, distance)
    _removeNode(graph, node)

def _addEdge(graph, first_node, second_node, value):
    '''add an edge from first_node to second_node '''
    graph[first_node][second_node] = value

def _get_backward_neighbours(graph, node):
    '''get all the nodes pointing to node'''
    tmp = dict()
    for current_node, adiacency in graph.items():
        if node in adiacency:
            tmp[current_node]=graph[current_node][node]
    return tmp

def _removeNode(graph, node):
    '''remove the node and take care of adiacency lists '''
    for current_node in copy.deepcopy(graph):
        if current_node is node:
            graph.pop(node)
        else:
            if node in graph[current_node]:
                graph[current_node].pop(node)

def add_shortcuts_to_graph(graph, importances, limit):
    '''given a limit remove all the nodes with smaller importance and add the relative shortcuts'''
    for node in copy.deepcopy(graph):
        if importances[node] < limit:
            _add_shortcut(graph, node)


g = {
    'A': {'B': 1, 'E': 2},
    'B': {'C': 2, 'E': 2},
    'C': {'D': 2},
    'D': {},
    'E': {'C': 2, 'D': 2},
}

importances = {
    'A': 5,
    'B': 1,
    'C': 4,
    'D': 3,
    'E': 1,
}

if __name__ == "__main__":
    add_shortcuts_to_graph(g,importances,2)
    if 'E' and 'B' not in g:
        print('contraction successfully completed')
