class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if n * m != len(original):
            return result
        
        idx = 0
        for i in range(m):
            res = []
            for j in range(n):
                res.append(original[idx])
                idx += 1
        
            result.append(res)
        
        return result