class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right


    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.remove(self.d[key])
        self.insert(self.d[key])

        return self.d[key].val


    def put(self, key: int, value: int) -> None:    
        if key in self.d:
            self.remove(self.d[key])

        self.d[key] = Node(key, value)
        self.insert(self.d[key])
        if len(self.d) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.d[lru.key]




        
