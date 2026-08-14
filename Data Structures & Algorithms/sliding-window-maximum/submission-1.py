"""
Approach:
Sliding window/max heap. Maintain a list and a heap.

We can't simply run max() for every window, as that would be O(n*k) runtime. We want O(n log k) at worst, or even O(n).

For each new number, we want to get rid of the old number, while also being able to easily update the maximum value.
A heap sounds good for the latter, while a list is good for the former.

We really only care about the max at each window, so if the element being removed from the window isn't the max,
we don't need to remove from the heap. The only time we need to remove from the heap is if we're removing the current
max value, and for a max heap, that's going to be O(1) time.

However, with this approach, as elements are not unique, an element can remain in the max heap even after it's left
the window. We can push both the value and its list index onto the heap. If we obtain a maximum that is outside of the
window, we can discard it until we get a max that is within the window.

nums=[9,10,9,-7,-4,-8,2,-6]
k=5



[9,10,9,-7,-4] -8 2 -6 | 10
(10,1) (9,0) (9,2) (-4,4) (-4,3)
9 [10,9,-7,-4,-8] 2 -6 | 10
(10,1) (9,0) (9,2) (-4,4) (-4,3)
9 10 [9,-7,-4,-8,2] -6 | 9
~(10,1) ~(9,0) (9,2) (-4,4) (-4,3)
9 10 9 [-7,-4,-8,2,-6] | 2

"""
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(0, k)]
        heapq.heapify(heap)
        maxima = [-heap[0][0]]
        for i in range(k, len(nums)):
            removed = -nums[i-k]
            if removed == heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < i-k+1:
                heapq.heappop(heap)
            maxima.append(-heap[0][0])
        return maxima