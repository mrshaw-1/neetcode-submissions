class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in dict1:
                dict1[k] = []
            dict1[k].append(i)


        return list(dict1.values())
