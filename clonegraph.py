from graph import graph_from_list, Node
from typing import Dict

old_ids = []


def create_clone(node: Node, cache: Dict[int, Node]) -> Node:
    if node.val not in cache:
        old_ids.append(id(node))
        copy = Node(node.val)
        cache[node.val] = copy
        for ng in node.neighbors:
            if ng.val not in cache:
                ncopy = create_clone(ng, cache)
            copy.neighbors.append(cache[ng.val])
    return cache[node.val]


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None
        cache = {}
        copy: Node = create_clone(node, cache)
        return copy


solution: Solution = Solution()


def assert_clone(node: Node):
    nid = id(node)
    print(f"assert not {nid} in {old_ids}")
    assert not nid in old_ids


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = graph_from_list(adjList)
    copy = solution.cloneGraph(node)
    breadth_first_graph(copy, assert_clone)
    breadth_first_graph(copy, print)
    print(f"copy {str(copy)}")
