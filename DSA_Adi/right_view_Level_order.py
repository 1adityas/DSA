
#https://leetcode.com/problems/binary-tree-right-side-view/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None :return []
        output=[]
        output=self.level_order(root,output)
        return output
        
    def level_order(self,root,output):
        q,output=deque() ,[]
        q.append(root)
        # output.append(root.val)
        l=1
        while len(q)!=0:
            no=q.popleft()
            l-=1
            if no.left:q.append(no.left)
            if no.right:q.append(no.right)
            if l==0:
                # print(root.val)
                output.append(no.val)
                l=len(q)
        return output