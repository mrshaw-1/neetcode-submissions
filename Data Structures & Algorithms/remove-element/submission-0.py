class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        nonValpos = 0
        k=0
        i=0
        for i in range(len(nums)):
            if nums[i] == val:
                counter+=1
            else:
                nums[nonValpos] = nums[i]
                nonValpos += 1
        k= len(nums) - counter
        return k