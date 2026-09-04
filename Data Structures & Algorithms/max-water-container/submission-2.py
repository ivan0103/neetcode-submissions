class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        h = min(heights[l], heights[r])
        res = h * (r-l)
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            # while l < len(heights) and  and heights[l+1] < heights[l]:
            #     l += 1
            # while r > 0 and heights[r] < heights[l] and heights[r-1] < heights[r]:
                
            h = min(heights[l], heights[r])
            res = max(res, h * (r-l))
        return res
