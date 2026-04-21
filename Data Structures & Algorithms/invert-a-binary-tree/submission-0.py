import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        q = collections.deque([cur])
        while len(q) > 0:
            n = q.popleft()
            if n is None:
                continue
            temp = n.left
            n.left = n.right
            n.right = temp
            q.append(n.left)
            q.append(n.right)
        return root