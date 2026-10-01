class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return sorted([i, nums.index(diff)])