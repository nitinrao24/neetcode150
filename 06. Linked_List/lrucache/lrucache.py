# leetcode 146
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Time Complexity: get -> O(1) , put -> O(1)
# Space Complexity: O(capacity)

# Simple doubly linked list node used by the cache
class Node:
    def __init__(self, key: int, value: int):
        self.key = key                  # store the key so we can delete from dict on eviction
        self.value = value              # store the value for this cache entry
        self.prev = None                # previous node in the DLL
        self.next = None                # next node in the DLL

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity        # maximum number of items the cache can hold
        self.cache = {}                 # hash map: key -> Node for O(1) access

        # Create sentinel (dummy) head and tail nodes to avoid edge-case checks
        self.head = Node(0, 0)          # least-recently-used end is head.next
        self.tail = Node(0, 0)          # most-recently-used end is tail.prev
        self.head.next = self.tail      # link head <-> tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If the key is not in cache, return -1
        if key not in self.cache:
            return -1

        node = self.cache[key]          # fetch the node in O(1)
        self._move_to_tail(node)        # mark as most recently used
        return node.value               # return its value

    def put(self, key: int, value: int) -> None:
        # If key already exists, just update value and move to MRU position
        if key in self.cache:
            node = self.cache[key]      # get the existing node
            node.value = value          # update its stored value
            self._move_to_tail(node)    # move it to the MRU position
            return

        # Otherwise we're inserting a brand new key
        if self.capacity == 0:          # edge case: zero-capacity cache
            return

        # If at capacity, evict the least-recently-used node (right after head)
        if len(self.cache) == self.capacity:
            lru = self.head.next        # node to evict (least recently used)
            self._remove(lru)           # unlink from the list
            del self.cache[lru.key]     # remove from the hash map

        # Create a new node for (key, value)
        node = Node(key, value)
        self.cache[key] = node          # record it in the hash map
        self._add_to_tail(node)         # place it at MRU position

    # ----- Doubly linked list helpers -----

    def _remove(self, node: Node) -> None:
        prev_node = node.prev           # node's previous neighbor
        next_node = node.next           # node's next neighbor
        prev_node.next = next_node      # bypass node forward
        next_node.prev = prev_node      # bypass node backward

    def _add_to_tail(self, node: Node) -> None:
        prev_last = self.tail.prev      # current last real node
        prev_last.next = node           # link last -> node
        node.prev = prev_last           # link node -> last
        node.next = self.tail           # link node -> tail sentinel
        self.tail.prev = node           # link tail <- node

    def _move_to_tail(self, node: Node) -> None:
        self._remove(node)              # unlink from current position
        self._add_to_tail(node)

class LRUCache1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)