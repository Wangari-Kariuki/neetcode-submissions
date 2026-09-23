class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *  (len(nums)) #the result is set to be the lenght of the input array

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  #prefix is the value at that position of the input array
            prefix *= nums[i] #pref is computed by muliplying the current by the value in that position
        postfix = 1
        for i in range (len(nums) -1, -1, -1 ):
            res[i] *= postfix
            postfix *= nums[i]
        return res
