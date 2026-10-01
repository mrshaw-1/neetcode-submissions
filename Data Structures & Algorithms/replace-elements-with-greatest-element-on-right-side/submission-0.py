class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        
        k = 0
        for i in range(len(arr)):
            LargestNum = 0
            if i != len(arr) - 1:
                for k in range(i+1, len(arr),1):
                    if arr[k] > LargestNum:
                        LargestNum = arr[k]
                arr[i] = LargestNum

            else:
                arr[i] = -1
        return arr
