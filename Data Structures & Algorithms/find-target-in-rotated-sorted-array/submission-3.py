class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # if Left half is sorted
                if nums[l] <= target < nums[mid]: # check whether the target is in the left half
                    r = mid - 1 #move the right to the left of the mid
                else:
                    l = mid + 1 # if the target is not in left half move the left to the right of mid
            else:  # if  Right half is sorted
                if nums[mid] < target <= nums[r]: #check whether the target is in left half
                    l = mid + 1 #if target is in right half , move the left to the right half
                else:
                    r = mid - 1# if target is not there move the right to the left half

        return -1
