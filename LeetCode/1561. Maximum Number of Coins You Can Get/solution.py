class Solution:
    def maxCoins(self, A):
        return sum(sorted(A)[len(A) // 3::2])        