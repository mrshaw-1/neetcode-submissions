class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0]*n
        suff = [0]*n
        ansLi = []


        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] + nums[i+1]

        for i in range(n):
            if pre[i] == suff[i]:
                ansLi.append(i)
            else:
                continue
        if ansLi == []:
            return -1
        else:
            return ansLi[0]