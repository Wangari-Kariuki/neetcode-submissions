class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        #max product of values at left and right index
         #get heights which when their distance/ index dif is multiplied by the mmin height among them, their product is max
        maxprod = 0
        minh = 0 
        for i, h in enumerate(heights):
            if i > 0 and h == heights[i - 1]:
                continue
            while l < r: 
                minh = min(heights[l], heights[r])
                dist = r - l
  #find the max by comparing the areas found in other loops 
 #while max product is not yet found move pointer at the shortest height
                maxprod = max(maxprod, minh * dist)
                if minh == heights[l]:
                    l += 1
                elif minh == heights[r]:
                    r -= 1
        return maxprod
