class Solution:
    # def isAnagram(self, str_a, str_b) -> bool:
    #     if len(str_a) != len(str_b): 
    #         return False
    #     map_a, map_b = {}, {}
    #     for i in range(len(str_a)):
    #         map_a[str_a[i]] = 1 + map_a.get(str_a[i],0)
    #         map_b[str_b[i]] = 1 + map_b.get(str_b[i],0)
    #     return map_a == map_b

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     group = []
    #     group.append([strs[0]])
    #     for i in range(1,len(strs)):
    #         match_found = False
    #         for j in range(len(group)):
    #             if self.isAnagram(strs[i], group[j][0]):
    #                 match_found = True
    #                 group[j].append(strs[i])
    #                 break
    #         if not match_found:
    #             group.append([strs[i]])
    #     return group

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
        return list(res.values())