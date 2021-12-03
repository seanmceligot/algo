from typing import Dict, Callable
from collections import deque
from typing import Dict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self):
        return f"{self.val} {[str(n.val) for n in self.neighbors]}"

def graph_from_list(adjList):
    nodes: Dict[int, Node] = {}
    for i in range(len(adjList)):
            nodes[i+1] = Node(i+1)
           
    val = 1
    for neighbors in adjList:
        for neighbor in neighbors:
            nodes[val].neighbors.append(nodes[neighbor])
        val+=1
    return nodes[1]

def breadth_first_graph(node: Node, proc: Callable[[Node], None] ): 
    visited = []
    queue = deque()
    if node is not None:
        queue.append(node)
        while len(queue) > 0:
            cur = queue.popleft()
            if not cur in visited:
                visited.append(cur)
                proc(cur)
                for ne in cur.neighbors:
                    queue.append(ne)
                    
