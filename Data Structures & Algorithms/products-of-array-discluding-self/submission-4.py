class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outlist=[1]*len(nums)
        left=[1]*len(nums)
        right=[1]*len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            outlist[i] = outlist[i]*left[i]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
            outlist[i] = outlist[i]*right[i]
        # for i in range(0,len(nums)):
        #     outlist[i] = left[i]*right[i]
        return outlist