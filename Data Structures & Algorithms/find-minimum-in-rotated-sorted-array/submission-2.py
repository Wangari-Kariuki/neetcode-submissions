class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the index of the minimum value is the value of rotation
        #left and right pointers for binary search 
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
