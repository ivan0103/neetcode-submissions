class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s.lower()))
        t_list = sorted(list(t.lower()))
        if s_list == t_list:
            return True
        else:
            return False