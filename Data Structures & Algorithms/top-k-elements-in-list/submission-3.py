class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        d_sorted = sorted(d, key = d.get, reverse=True)

        res = list()
        for i in range(k):
            res.append(d_sorted[i])

        return res;