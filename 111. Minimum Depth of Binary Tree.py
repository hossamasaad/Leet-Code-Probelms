class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        q = []
        if root:
            q.append(root)
        
        lvl = 0

        while q:
            lvl += 1

            n = len(q)
            new_q = []

            for i in range(n):
                curr = q[i]

                if not curr.left and not curr.right:
                    return lvl

                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
                
            
            q = new_q
            