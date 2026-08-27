class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        out = []
        for num in nums:
            if num in num_count:
               num_count[num] += 1
            else: 
                num_count[num] = 1
        
        return(heapq.nlargest(k, num_count))
