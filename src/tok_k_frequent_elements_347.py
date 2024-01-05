# Given an integer array nums and an integer k,
# return the k most frequent elements. You may
# return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        buckets = [list() for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        sol = []
        for bucket in reversed(buckets):
            for val in bucket:
                sol.append(val)
                k -= 1
                if k == 0:
                    return sol
