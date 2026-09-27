from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num]+=1
        sorted_keys = sorted(hashMap, key = hashMap.get, reverse = True)

        return sorted_keys[:k]

        



        

