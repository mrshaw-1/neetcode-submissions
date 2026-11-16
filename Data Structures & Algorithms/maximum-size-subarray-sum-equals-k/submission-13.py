class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pre=[0]*n
        val = 0
        dict1={0:-1}

        pre[0]=nums[0]
        if pre[0] not in dict1:
            dict1[pre[0]] = 0


        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
            if pre[i] not in dict1:
                dict1[pre[i]] = i

        for i in range(n):
            end = pre[i]-k
            if end in dict1:
                temp = i - dict1[end]
                val = max(temp, val)
        
        return val