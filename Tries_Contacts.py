
class node(object):
    __slots__ = ['data', 'num', 'children']
    def __init__(self, data=None):
        self.data = data
        self.num = 0
        self.children = {}

class trie(object):
    def __init__(self):
        self.root = node('*')
        # print('root established')
    def add_word(self, foo):
        current = self.root
        current.num += 1 
        for char in foo:
            if char not in current.children:
                # create in new node
                current.children[char] = node(char)
            current = current.children[char]
            current.num += 1 
    def lookup(self, foo):
        current = self.root
        for char in foo:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.num

t = trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        t.add_word(contact)
    if op == 'find':
        print(t.lookup(contact))