from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i,j):
            if i < j:
                return 0
            if j == 0:
                return 1
            return dfs(i-1,j) + (dfs(i-1,j-1) if s[i-1]==t[j-1] else 0)
        return dfs(len(s),len(t))