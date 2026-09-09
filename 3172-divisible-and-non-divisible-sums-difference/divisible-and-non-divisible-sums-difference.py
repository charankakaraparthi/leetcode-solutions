class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2

        q = n // m
        num2 = m * q * (q + 1) // 2

        return total - 2 * num2