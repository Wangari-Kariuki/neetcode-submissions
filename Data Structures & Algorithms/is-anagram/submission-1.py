class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for  i in range(len(s)):
            # counting occurrences of  characters in each string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # checking if counter characters are the same for both strings
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True