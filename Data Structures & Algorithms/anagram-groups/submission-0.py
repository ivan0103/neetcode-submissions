class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list);
        for word in strs:
            count = {}
            for l in word:
                if (l in count):
                    count[l] = count[l] + 1;
                else:
                    count[l] = 1;
            key = tuple(sorted(count.items()))
            res[key].append(word)
        return list(res.values());
