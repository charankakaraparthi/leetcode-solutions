class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Sort by the squared value in descending order
        nums.sort(key=lambda x: x * x, reverse=True)
        
        n = len(nums)
        mid = (n + 1) // 2
        
        # Add the first half (largest squares) and subtract the second half (smallest squares)
        return sum(x * x for x in nums[:mid]) - sum(x * x for x in nums[mid:])