# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        averages = []
        q = []

        if root:
            q.append(root)
        
        while q:
            n = len(q)
            avg = 0.0
            new_q = []

            for i in range(n):
                curr = q[i]
                avg += curr.val
                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)
            
            averages.append(avg / n)
            q = new_q

        return averages