class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        ans = 0
        freq = {0:1}
        for i in range(n):
            prefix += nums[i]
            if prefix - k in freq:
                ans += freq[prefix - k]
            freq[prefix] = freq.get(prefix, 0) + 1
        return ans 
