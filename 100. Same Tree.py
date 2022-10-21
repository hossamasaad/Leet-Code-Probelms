# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    
        queue1 = []
        queue2 = []

        if p:
            queue1.append(p)
        if q:
            queue2.append(q)

        if len(queue1) != len(queue2):
                return False

        while queue1 and queue2:
            
            new_queue1 = []
            new_queue2 = []
            
            if len(queue1) != len(queue2):
                return False

            for i in range(len(queue1)):
                curr1, curr2 = queue1[i], queue2[i]
                
                if curr1.val == curr2.val:
                    if curr1.left:
                        new_queue1.append(curr1.left)
                    else:
                        if curr2.left is not None:
                            return False

                    if curr1.right:
                        new_queue1.append(curr1.right)
                    else:
                        if curr2.right is not None:
                            return False
                    
                    if curr2.left:
                        new_queue2.append(curr2.left)
                    else:
                        if curr1.left is not None:
                            return False

                    if curr2.right:
                        new_queue2.append(curr2.right)
                    else:
                        if curr1.right is not None:
                            return False
                else:
                    return False
            
            queue1 = new_queue1
            queue2 = new_queue2

        return True