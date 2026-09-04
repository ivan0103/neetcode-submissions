class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            h = min(heights[l], heights[r])
            res = max(res, h * (r-l))

            while l < r and heights[l] <= h:
                l += 1
            while l < r and heights[r] <= h:
                r -= 1

        return res
