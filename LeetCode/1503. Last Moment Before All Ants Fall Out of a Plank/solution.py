class Solution:
    def getLastMoment(self, n, left, right):
        return max(max(left or [0]), n - min(right or [n]), 0)