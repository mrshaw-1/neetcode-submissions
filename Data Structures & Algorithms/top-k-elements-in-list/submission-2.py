class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        count = 0
        tempLi = []
        tempLi2 = []
        for i in nums:
            if i not in dict1:
                dict1[i] = []
                count += 1
                dict1[i] = count
                count=0
            elif i in dict1:
                dict1[i] += 1
                count=0
        tempLi = sorted(dict1, key=dict1.get, reverse=True)
        return tempLi[0:k]
