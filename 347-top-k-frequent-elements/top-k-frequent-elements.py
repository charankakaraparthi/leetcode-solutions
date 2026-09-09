class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        # Get k most frequent elements
        ans = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        return ans