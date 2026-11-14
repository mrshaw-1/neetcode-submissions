class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        
        for i in set_nums:
            if (i-1) not in set_nums:
                key = i
                alen = 1
                longest = max(longest, alen)
                while(key+1 in set_nums):
                    alen+=1
                    longest = max(longest, alen)
                    key = key+1
        if (len(nums) == 0):
            return 0
        else:
            return longest