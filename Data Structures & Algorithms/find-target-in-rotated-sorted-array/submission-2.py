# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         #two sum and binary search of a rotated array
#         for i, n  in enumerate(nums):
#             l = 0
#             r = len(nums) - 1
            # mid = len(nums)  // 2
            # if i > 0 and n == nums[i-1]:
            #     continue
            #for each index compare the element with the target
            #we check whether the target is in one of the halfs then we discard the other half
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
