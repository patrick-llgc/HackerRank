""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_2(root):
    return check(root, -float("inf"), float("inf"))

def check(root, minval, maxval):
    """We need not only to check the order, but also the limit too"""
    if root is None:
        return True
    if root.data >= maxval or root.data <= minval:
        return False
    return check(root.left, minval, root.data) and check(root.right, root.data, maxval)


def check_binary_search_tree_(root):
    arr = traverse(root, [])
    if not arr:
        return True
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True
    
def traverse(root, arr):
    if root is None:
        return arr
    if root.left is not None:
        arr = traverse(root.left, arr)
    arr.append(root.data)
    if root.right is not None:
        arr = traverse(root.right, arr)
    return arr