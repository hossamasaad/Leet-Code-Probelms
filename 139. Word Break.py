class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        
        if not s:
            return True
        if not wordDict:
            return False
        
        dp = [True] + [False for i in range(len(s))]
        maxlen = len(max(wordDict, key=len))

        for i in range(1, len(s)+1):
            for j in range(i-1, max(i-maxlen-1, -1), -1):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        
        return dp
