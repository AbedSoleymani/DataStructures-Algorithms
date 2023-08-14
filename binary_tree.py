class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')


def dfs_search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    return dfs_search(node.left, target) or dfs_search(node.right, target)


from collections import deque
def bfs_search(node, target):
    if node is None:
        return False
    
    queue = deque([node])
    while queue:
        current_node = queue.popleft()
        if current_node.value == target:
            return True
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return False


""" sample binary tree:
       1
  2        3
4  5     7   0
"""
if __name__ == "__main__":
    import os
    os.system("clear")

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(0)

    print("In-order traversal:")
    in_order_traversal(root)

    print("\n\nPre-order traversal:")
    pre_order_traversal(root)

    print("\n\nPost-order traversal:")
    post_order_traversal(root)

    target_value = 3
    if dfs_search(root, target_value):
        print("\n\n{} found in the tree.".format(target_value))
    else:
        print("\n\n{} not found in the tree.".format(target_value))

    target_value = 9
    if bfs_search(root, target_value):
        print("\n\n{} found in the tree.".format(target_value))
    else:
        print("\n\n{} not found in the tree.".format(target_value))