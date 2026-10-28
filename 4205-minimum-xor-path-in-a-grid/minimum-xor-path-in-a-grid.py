class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [set() for _ in range(n)]
        
        for i in range(m):
            new_dp = [set() for _ in range(n)]
            for j in range(n):
                curr_val = grid[i][j]
                prev_sets = []
                
                if i > 0:
                    prev_sets.append(dp[j])
                if j > 0:
                    prev_sets.append(new_dp[j - 1])
                
                if not prev_sets:
                    new_dp[j] = {curr_val}
                else:
                    combined = set()
                    for s in prev_sets:
                        for x in s:
                            combined.add(x ^ curr_val)
                    new_dp[j] = combined
            dp = new_dp
            
        return min(dp[n - 1])