class DLNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lruSentinel = DLNode()
        self.lruSentinel.key = -1
        self.mruSentinel = DLNode()
        self.mruSentinel.key = 1001
        self.lruSentinel.next = self.mruSentinel
        self.mruSentinel.prev = self.lruSentinel

    def _append_to_mru(self, node: DLNode):
        oldNode = self.mruSentinel.prev
        oldNode.next = node
        node.next = self.mruSentinel
        self.mruSentinel.prev = node
        node.prev = oldNode

    def _move_to_mru(self, node: DLNode):
        leftNode = node.prev
        rightNode = node.next
        leftNode.next = rightNode
        rightNode.prev = leftNode
        self._append_to_mru(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if node.next != self.mruSentinel:
            self._move_to_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_mru(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.lruSentinel.next.key]
                nodeToSkipTo = self.lruSentinel.next.next
                self.lruSentinel.next = nodeToSkipTo
                nodeToSkipTo.prev = self.lruSentinel
            node = DLNode()
            node.key = key
            node.val = value
            self.cache[key] = node
            self._append_to_mru(node)
                
