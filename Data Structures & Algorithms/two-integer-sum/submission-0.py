class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #value : index

        for i , n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i] # pair of indices
            prevMap[n] = i #if no solution is found update the map
        return
