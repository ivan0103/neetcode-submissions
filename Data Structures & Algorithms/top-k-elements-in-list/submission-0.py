from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        res = []

        for i in range(k):
            res.append(sorted_count[i])

        return res