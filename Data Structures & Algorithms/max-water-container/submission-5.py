class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0
        while i < j:
            h = min(heights[i], heights[j])
            area = max(area, h * (j-i))
            while i < j and heights[i] <= h:
                i += 1
            while i < j and heights[j] <= h:
                j -= 1
        return area
