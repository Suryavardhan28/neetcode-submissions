class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map = {}
        # res = []
        # for i in nums:
        #     map[i] = map.get(i,0) + 1
        # for i in range(k):
        #     hf = -1
        #     hn = -1
        #     for j in map.keys():
        #         if map[j] > hf:
        #             hf = map[j]
        #             hn = j
        #     map.pop(hn)
        #     res.append(hn)
        # return res

        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1

        arr = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            arr[cnt].append(num)
        
        res = []
        for i in range(len(arr) - 1, 0 , -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res