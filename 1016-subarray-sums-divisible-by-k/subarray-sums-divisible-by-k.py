class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        ans = 0
        f = {0:1}
        for i in range(n):
            prefix = prefix + nums[i]
            remainder = prefix % k
            if remainder in f:
                ans += f[remainder]
            f[remainder] = f.get(remainder, 0) + 1
        return ans

        