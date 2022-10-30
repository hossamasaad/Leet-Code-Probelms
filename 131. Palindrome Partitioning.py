class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []

        def is_palindrome(string): 
            return string == string[::-1]

        def search(res, curr_s, idx):
            if idx == len(s):
                if is_palindrome(curr_s):
                    if len(curr_s) > 0:
                        res.append(curr_s)
                        results.append(res)
                return
            
            curr_s += s[idx]
            search(res[:], curr_s, idx+1)

            if is_palindrome(curr_s):
                res.append(curr_s)
                search(res[:], "", idx+1)
        
        
        search([], "", 0)
        return results