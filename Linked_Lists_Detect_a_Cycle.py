"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle1(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while (fast != slow):
        # make sure fast.next and fast exist
        if fast is None or fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
    return True

def has_cycle(head):
    """Keep a still pointer, and look up to 100 steps ahead using moving pointer"""
    if head is None:
        return False
    still = head
    moving = head.next
    while still is not None:
        i = 0
        while i < 101 and moving is not None:
            if still == moving:
                return True
            moving = moving.next
            i = i + 1
        still = still.next
    return False
    
