import typing
import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        

        counter = collections.defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        print("counter", counter)
        counts = [[] for n in nums]
        counts += []

        for key, v in counter.items():
            counts[v].append(key)
        
        print("counts", counts)
        result = []
        while len(result) < k:
            result.extend(counts.pop())
        
        return result[0:k]


input = ([1,1,1,2,2,3], 2)
s = Solution()
print(s.topKFrequent(*input))

