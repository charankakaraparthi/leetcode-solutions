class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result
            

        