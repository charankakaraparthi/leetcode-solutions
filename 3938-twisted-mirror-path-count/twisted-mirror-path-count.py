class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        def get_landing(r: int, c: int, move_dir: int):
            cr = r
            cc = c
            d = move_dir # 1 for right, 0 for down
            
            while 0 <= cr < m and 0 <= cc < n and grid[cr][cc] == 1:
                if d == 1:
                    cr += 1
                    d = 0
                else:
                    cc += 1
                    d = 1
            
            if not (0 <= cr < m and 0 <= cc < n):
                return (-1, -1, -1)
            return (cr, cc, d)

        dp_grid = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        # Initialize starting valid transitions from (0, 0)
        for d in (0, 1):
            nr = 1 if d == 0 else 0
            nc = 0 if d == 0 else 1
            if 0 <= nr < m and 0 <= nc < n:
                tr, tc, td = get_landing(nr, nc, d)
                if tr != -1:
                    dp_grid[tr][tc][td] = (dp_grid[tr][tc][td] + 1) % MOD

        for r in range(m):
            for c in range(n):
                for d in (0, 1):
                    curr_ways = dp_grid[r][c][d]
                    if curr_ways == 0:
                        continue
                    if r == m - 1 and c == n - 1:
                        continue
                    
                    for out_d in (0, 1):
                        nr = r + (1 if out_d == 0 else 0)
                        nc = c + (0 if out_d == 0 else 1)
                        if 0 <= nr < m and 0 <= nc < n:
                            tr, tc, td = get_landing(nr, nc, out_d)
                            if tr != -1:
                                dp_grid[tr][tc][td] = (dp_grid[tr][tc][td] + curr_ways) % MOD

        return (dp_grid[m - 1][n - 1][0] + dp_grid[m - 1][n - 1][1]) % MOD