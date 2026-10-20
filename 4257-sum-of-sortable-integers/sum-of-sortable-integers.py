class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])
            
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        ans = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            sortable = True
            
            for start in range(0, n, k):
                end = start + k - 1
                
                if start > 0 and pref_max[start] > suff_min[start]:
                    sortable = False
                    break
                    
                internal_drops = 0
                if k > 1:
                    internal_drops = pref_drop[end] - pref_drop[start]
                
                circular_drop = 1 if nums[end] > nums[start] else 0
                
                if internal_drops + circular_drop > 1:
                    sortable = False
                    break
                    
            if sortable:
                ans += k
                
        return ans