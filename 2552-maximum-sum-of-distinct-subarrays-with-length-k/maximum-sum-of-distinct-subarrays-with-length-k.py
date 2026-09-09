class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        left = 0
        window_sum = 0
        ans = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            window_sum += nums[right]

            if right - left + 1 > k:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                ans = max(ans, window_sum)

        return ans