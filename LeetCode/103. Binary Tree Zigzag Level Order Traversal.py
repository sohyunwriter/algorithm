# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        dq = deque([root])
        sig = 1
        
        while dq:
            visited = []
            for i in range(len(dq)):
                curnode = dq.popleft()
                if curnode.left:
                    dq.append(curnode.left)
                if curnode.right:
                    dq.append(curnode.right)
                visited.append(curnode.val)
            
            if sig:
                ans.append(visited)
            else:
                ans.append(reversed(visited))
            sig ^= 1  # bit operator (0^1=1, 1^1=0)
        return ans
