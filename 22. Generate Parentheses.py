class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        def search(stack, s):
            if len(s) == n * 2:
                if len(stack) == 0:
                    results.append(s)
                return

            if len(stack) > n:
                return
            
            stack.append("(")
            search(stack, s+"(")
            stack.pop()

            if len(stack) > 0:
                tmp = stack.pop()
                search(stack, s+")")
                stack.append(tmp)

        search([], "")
        return results