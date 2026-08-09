class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0) #get frequency of each element in the array
        for n , c in count.items():
            freq[c].append(n) #fo each count/ frequency append array elements with that count
        res = []
        for i in range(len(freq) -1, 0, -1): #for each sublist
            for n in freq [i]:
                res.append(n) #append values into result list 
                if len(res) == k: #check if lenght of the result is k 
                    return res

