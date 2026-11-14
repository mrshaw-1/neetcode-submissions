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
                blen=0
                while(i+alen in set_nums):
                    blen+=1
                    dic[key] = max(alen, blen)
                    i = i+alen

            elif i not in dic:
                continue
        if (len(nums) == 0):
            return 0
        else:
            longest = max(dic.values())
        return longest+1
        
