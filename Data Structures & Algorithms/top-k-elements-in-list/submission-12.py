class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for i in nums:
            map[i] = map.get(i,0) + 1
        for i in range(k):
            hf = -1
            hn = -1
            for j in map.keys():
                if map[j] > hf:
                    hf = map[j]
                    hn = j
            map.pop(hn)
            res.append(hn)
        return res