

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key,v in hashmap.items():
            buckets[v].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result