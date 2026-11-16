class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        pre = [0]*len(nums)
        suff = [0]*len(nums)
        val = float('-inf')

        pre[0] = nums[0]
        suff[len(nums)-1] = nums[len(nums)-1]

        for i in range (1, len(nums)):
            pre[i] = pre[i-1] + nums[i]
        
        for i in range (len(nums)-2,-1,-1):
            suff[i] = suff[i+1] + nums[i]

        for i in range (len(nums)):
            temp = max(pre[i], suff[i])
            val = max(val, temp)
        return val
