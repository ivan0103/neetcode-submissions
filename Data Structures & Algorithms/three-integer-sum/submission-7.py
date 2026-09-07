class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if v > 0:
                break;
            if i > 0 and v == nums[i-1]:
                continue
            s = i + 1
            e = len(nums)-1
            while s < e:
                cur_sum = v + nums[s] + nums[e]
                if cur_sum == 0:
                    res.append([v,nums[s],nums[e]])
                    s += 1
                    e -= 1
                    while nums[s] == nums[s - 1] and s < e:
                        s += 1
                elif cur_sum < 0:
                    s += 1
                elif cur_sum > 0:
                    e -= 1
        return res
                