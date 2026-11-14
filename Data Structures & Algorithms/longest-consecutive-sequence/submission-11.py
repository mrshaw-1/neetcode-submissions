class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        seq_nums = [x for x in set_nums if (x-1) not in set_nums]
        dic = {x:0 for x in seq_nums}
        longest = 0
        
        for i in set_nums:
            if i in dic:
                key = i
                alen = 1
                longest = max(longest, alen)
                while(i+1 in set_nums):
                    alen+=1
                    longest = max(longest, alen)
                    dic[key] = alen
                    i = i+1

            elif i not in dic:
                continue
        if (len(nums) == 0):
            return 0
        else:
            return longest
        
