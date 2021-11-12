from typing import List, Optional
# Python3 program to construct tree using
# inorder and postorder traversals

# Helper function that allocates
# a new node
class Node:
    def __init__(self, data:int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    def __repr__(self):
        return  str(self.data)
# Recursive function to construct binary
# of size n from Inorder traversal in[]
# and Postorder traversal post[]. Initial
# values of inStrt and inEnd should be
# 0 and n -1. The function doesn't do any
# error checking for cases where inorder
# and postorder do not form a tree
def build_node(desc: str, inorder_list: List[int], postorder_list: List[int], inorder_start:int, inoder_end:int, root_node_index: List[int]):
    # Base case
    if (inorder_start > inoder_end):
        return None

    print(f"{desc}: inorder s={inorder_start} e:{inoder_end} {inorder_list[inorder_start:inoder_end]}")
    print(f"{desc}: post    s={inorder_start} e:{inoder_end} {postorder_list[0:root_node_index[0]+1]}")
    # Pick current node from Postorder traversal
    # using postIndex and decrement postIndex
    node = Node(postorder_list[root_node_index[0]])

    print(f"root [{root_node_index[0]}] = node: {node}")
    root_node_index[0] -= 1

    # If this node has no children
    # then return
    if (inorder_start == inoder_end):
        print(f"return {desc}: node {node}")
        return node

    # Else find the index of this node
    # in Inorder traversal
    inorder_found_index = search(inorder_list, inorder_start, inoder_end, node.data)

    # Using index in Inorder traversal,
    # construct left and right subtress
    node.right = build_node("right", inorder_list, postorder_list, inorder_found_index + 1, inoder_end, root_node_index)
    node.left = build_node("left", inorder_list, postorder_list, inorder_start, inorder_found_index - 1, root_node_index)
    print(f"right {node.right}\n")
    print(f"left {node.left}\n")
    return node

def buildTree(In: List[int], post: List[int], n: int):
    root_node_index = [n - 1]
    return build_node("start", In, post, 0, n - 1, root_node_index)

# Function to find index of value in arr[start...end]. 
# The function assumes that value is postsent in in[]
def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value): break
    return i

def preOrder(node):
    if node == None:
        return
    print(node.data,end=" ")
    preOrder(node.left)
    preOrder(node.right)

# Driver code
if __name__ == '__main__':
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    n = len(In)

    root = buildTree(In, post, n)

    print("Preorder of the constructed tree :")
    preOrder(root)

# This code is contributed by PranchalK
