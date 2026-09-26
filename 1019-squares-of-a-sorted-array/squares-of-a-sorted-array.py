class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result