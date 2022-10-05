# LRU Cache https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

# Use doubly linked list: append O(1)
class Node:
    def __init__(self, k, v):  # One node takes in 2 values; both prev and next pointers exist: doubly linked list
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:  # The dic and the doubly linked list run in parallel and do not affect each other
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()  # same as '{}'
        self.head = Node(0, 0)  # head and tail are just nominal nodes
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # for get() and put(): every time we access an existing key-value pair, we need to remove it then append it to the end
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)  # self defined function, see below
            self._add(n)  # self defined function, see below
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)  # 1.append to doubly linked list
        self.dic[key] = n  # 2.add to dic
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)  # 1.pop_first from doubly linked list
            del self.dic[n.key]  # 2.delete from dic

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):  # basically append
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)