class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {} # key -> key and value -> node(k, v)[will point to the noode]
        
        # To maintain LRU and Most Recently Used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.size < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        

        