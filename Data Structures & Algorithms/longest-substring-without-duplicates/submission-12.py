class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        substring = ""
        for j, c in enumerate(s):
            if c not in substring:
                substring = s[i:j+1]
                res = max(res, len(substring))
            else:
                i = s.find(c, i , j) + 1
                substring = s[i: j +1]
        return res