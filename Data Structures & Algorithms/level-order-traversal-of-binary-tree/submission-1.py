import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([(root, 0)])
        res = collections.defaultdict(list)
        while len(q) > 0:
            r = q.popleft()
            if r[0] is None:
                continue
            res[r[1]].append(r[0].val)
            q.append((r[0].left, r[1] + 1))
            q.append((r[0].right, r[1] + 1))
        return list(res.values())