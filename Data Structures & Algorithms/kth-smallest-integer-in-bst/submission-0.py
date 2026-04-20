import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = collections.deque([root])
        arr = []
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                continue
            arr.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        arr.sort()
        return arr[k-1]