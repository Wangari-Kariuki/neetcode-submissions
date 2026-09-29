class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        charset = set()
        l = 0
        r = len(s) - 1
        res = 0
        for r in range(len(s)):
            while s[r] in charset: #check whether the value on right pointer is already in the unique set 
                charset.remove(s[l]) # remove the value on the 
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)# the lenghtof the longest interval
        return res 
        



