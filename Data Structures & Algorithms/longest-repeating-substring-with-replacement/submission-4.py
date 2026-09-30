class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #replace to atmost k times
        #return the longest string of same characters
        #replace that occur less frequently
        # we want characters in a window to match the most frequent char in that window
        l = 0
        res = 0
        count1 = {}
        maxf = 0
            #as long as our no_rep is less than or equal to k , perform replacement on no_rep
        for r in range(len(s)):
           
            count1[s[r]] = 1 + count1.get(s[r], 0)
            maxf = max(maxf, count1[s[r]])
            #beffore updating result check whether window is valid 
            while (r-l + 1) - maxf > k: #window is not valid if no of is greater than k
                count1[s[l]] -= 1
                l += 1

            res = max(res, r-l +1)
        return res

