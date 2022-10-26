class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def search(idx, sum, comb):
            if len(comb) == k:
                if sum == n:
                    res.append(comb)
                else:
                    return
            
            else:
                for i in range(idx, k):
                    comb.append(i)
                    search(idx+1, sum+i, comb)
                    comb.pop()
        
        search(0, 0, [])
        return res