class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        current = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1

            ans = max(ans, current)

        return ans