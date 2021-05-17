from heap import binheap
from math import inf

def dijkstra(graph, source, *finish):
    '''dijsktra standard implementation. Graph should be given as {node:adiacency list}.
       Final destination is optional'''

    predecessors = {node: None for node in graph}
    distances = {node : inf for node in graph}
    distances[source] = 0
    priory_queue = binheap(list(distances.items()), total_order = pair_order)
    
    def relax(current_node, neighbour, distance):
        '''update the distances'''
        if priory_queue.get_distance(neighbour) is not None and priory_queue.get_distance(neighbour) > distances[current_node] + distance:
            priory_queue.decrease_key(neighbour, distances[current_node] + distance) 
            predecessors[neighbour] = current_node

    while priory_queue: 
        current_node, current_distance = priory_queue.remove_minimum()
        distances[current_node] = current_distance
        if finish and finish[0] is current_node:
                return distances[current_node], predecessors[current_node]
        for neighbour, distance in graph[current_node].items():
            relax(current_node, neighbour, distance)
    return distances, predecessors
        
def pair_order(A, B):
    return A[1] < B[1]

if __name__ == "__main__":
    g = {'A': {'B': 5, 'D': 9, 'E': 2}, 
    'B': {'C': 2}, 'D': {},
    'C': {'D': 3}, 'E': {'F': 3},
    'F': {'D': 2}
    }
    
    distances, predecessors = dijkstra(g, 'A')
    print('distances are', distances)
    print('predessesors are', predecessors)



