class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: #for each string in the list
            count = [0] * 26 #create  a list from 0 to 26
            for c in s: #for each character in each string
                count[ord(c) - ord("a")] += 1 #obtain its alue in list of 26 by getting differece between its ASCII value and the ASCII value of "a"
            res[tuple(count)].append(s) #group strings with particular count together
        return list(res.values())

        #O(m * n)
        