class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in dic:
                dic[sorted_str].append(i)
            else:
                dic[sorted_str]=[i]
        return dic.values()