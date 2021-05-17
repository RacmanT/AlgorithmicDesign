from heap import binheap
from shortcuts import _get_backward_neighbours, add_shortcuts_to_graph
from math import  inf
import copy

# Author: Tibor Racman
# Date: 16/05/2021
# Description: Third Assignament question 2.b

def _reverse_graph(graph):
    '''compute the reverse graph by turning the arrows direction'''
    graph_star = copy.deepcopy(graph)
    for node in graph:
        tmp = {}
        for adiancent in _get_backward_neighbours(graph, node):
                tmp[adiancent] = graph[adiancent][node]
        graph_star[node]=tmp
    return graph_star

def pair_order(A, B):
    return A[1] < B[1]

def contraction_hierarchies(graph, start, finish):
    '''Contraction hierarchy algorithm with bidirectional Dijkstra'''
    graph_inverse = _reverse_graph(g)

    #init forward dijkstra
    predecessors = {node: None for node in graph_inverse}
    distances = {node : inf for node in graph}
    distances[start] = 0
    priory_queue = binheap(list(distances.items()), total_order = pair_order)
    visited = list()

    #init backward dijkstra
    predecessors_back = {node: None for node in graph_inverse}
    distances_back = {node : inf for node in graph_inverse}
    distances_back[finish] = 0
    priory_queue_back = binheap(list(distances_back.items()), total_order = pair_order)
    visited_back = list()
    
    def relax(current_node, neighbour, current_distance, forward=True):
        '''updating the distances both for forward and backward dijkstra'''
        if forward:
            if priory_queue.get_distance(neighbour) is not None and priory_queue.get_distance(neighbour) > distances[current_node] + current_distance:
                priory_queue.decrease_key(neighbour, distances[current_node] + current_distance) 
                predecessors[neighbour] = current_node
        else:
            if priory_queue_back.get_distance(neighbour) is not None and priory_queue_back.get_distance(neighbour) > distances_back[current_node] + current_distance:
                priory_queue_back.decrease_key(neighbour, distances_back[current_node] + current_distance) 
                predecessors_back[neighbour] = current_node

    while priory_queue and priory_queue_back: 

        current_node, current_distance = priory_queue.remove_minimum()
        visited.append(current_node)
        distances[current_node] = current_distance

        current_node_back, current_distance_back = priory_queue_back.remove_minimum()
        visited_back.append(current_node_back)
        distances_back[current_node_back] = current_distance_back

        if current_node in visited_back:
            return distances[current_node] + distances_back[current_node]
        elif current_node_back in visited:
            return distances[current_node_back] + distances_back[current_node_back]

        #contracting the graph using the current node as importance limit
        add_shortcuts_to_graph(graph, importances, importances[current_node])
        add_shortcuts_to_graph(graph_inverse, importances, importances[current_node_back])   

        for neighbour, distance in graph[current_node].items():
            relax(current_node, neighbour, distance)
        
        for neighbour_back, distance_back in graph_inverse[current_node_back].items():
            relax(current_node_back, neighbour_back, distance_back, forward = False)


if __name__ == "__main__":
    g = {
    'A': {'B': 1, 'E': 2},
    'B': {'C': 2, 'E': 2},
    'C': {'E': 1},
    'D': {'C':2},
    'E': {'D': 5},
    }

    importances = {
    'A': 3,
    'B': 1,
    'C': 1,
    'D': 3,
    'E': 12,
    }
    print(contraction_hierarchies(g, 'A', 'D'))