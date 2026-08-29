import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        result = [x[0] for x in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
 
        return result    