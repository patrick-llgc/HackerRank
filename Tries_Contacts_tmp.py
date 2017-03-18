"""
from collections import defaultdict
n = int(input().strip())
namedict = defaultdict(int)
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        namedict[contact] += 1
    if op == 'find':
        counter = 0
        for name in namedict.keys():
            if name.startswith(contact):
                counter += namedict[name]
        print(counter)

"""

class node(object):
    __slots__ = ['data', 'num', 'children']
    def __init__(self, data=None):
        self.data = data
        self.num = 0
        self.children = {}
    def expand(self):
        if len(self.data) <= 1:
            return
        self.data = self.data[0]
        self.num += 1
        self.children[self.data[1:]] = node(self.data[1:])

class trie(object):
    def __init__(self):
        self.root = node('*')
        # print('root established')
    def add_word2(self, foo):
        current = self.root
        current.num += 1 
        for char in foo:
            if char not in current.children:
                # create in new node
                current.children[char] = node(char)
            current = current.children[char]
            current.num += 1 
    def add_word(self, foo):
        current = self.root
        current.num += 1 
        for i in range(len(foo)):
            char = foo[i]
            for child in current.children.values():
                child.expand()
            if char not in current.children:
                current.children[foo[i:]] = node(foo[i:])
                break
            else:
                current = current.children[char]
                current.num += 1
    def lookup(self, foo):
        current = self.root
        for char in foo:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.num


string = "hackerrank"
print(string)
t = trie()
t.add_word(string)
for i in range(200000):
    t.add_word('hackex')
t.add_word('xhackey')

num = t.lookup('hack')
print(num)