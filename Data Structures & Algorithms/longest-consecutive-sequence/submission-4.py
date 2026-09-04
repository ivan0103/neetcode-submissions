class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 0
        for i in n:
            if i-1 not in n:
                length = 1
                while i + length in n:
                    length += 1
                res = max(res, length) 
        return res