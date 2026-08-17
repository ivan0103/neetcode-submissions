class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = defaultdict(int);
        for i,n in enumerate(nums):
            diff = target - n;
            if diff in diffmap:
                return [diffmap[diff], i];
            else:
                diffmap[n] = i;