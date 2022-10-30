class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"     ],
            "9":["w", "x", "y", "z"]
        }
        
        results = []
        def go(s):
            if len(s) == len(digits):
                results.append(s)
                return
                
            idx = len(s)
            for letter in letters[digits[idx]]:
                go(s + letter)

        if len(digits) > 0:
            go("")
        return results