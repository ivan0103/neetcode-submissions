class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;

        dictS = defaultdict();
        for l in s:
            if l in dictS:
                dictS[l] = dictS[l] + 1;
            else:
                dictS[l] = 1;
        
        for l in t:
            if l not in dictS:
                return False;
            else:
                dictS[l] = dictS[l] - 1;
                if dictS[l] < 0:
                    return False;

        return True;