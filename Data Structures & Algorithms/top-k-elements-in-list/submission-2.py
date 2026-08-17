class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int);

        for i in nums:
            count[i] += 1;
        
        sorted_count = sorted(count, key=count.get, reverse=True)

        ans = list();
        for i in range(k):
            ans.append(sorted_count[i]);
        
        return ans;