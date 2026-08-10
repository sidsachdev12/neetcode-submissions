import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)

        # print(heap, max_heap)
        while heap and len(heap) > 1:
            # print(heap)
            a = -1 * heapq.heappop(heap)
            b = -1 * heapq.heappop(heap)

            if a == b:
                continue
            
            res = abs(a-b)
            heapq.heappush(heap, -1 * res)

        return 0 if not heap else -1 * heapq.heappop(heap)

# [2, 2, 3, 4, 6]
# [2, 2, 2, 3]
# [1, 2, 2]
# [1]