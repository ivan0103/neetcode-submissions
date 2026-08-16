class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            sorts = ''.join(sorted(s))
            ans[sorts].append(s)
        
        return list(ans.values())
