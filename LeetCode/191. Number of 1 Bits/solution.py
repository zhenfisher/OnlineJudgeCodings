class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            # n -= (n & (-n))
            n &= (n-1)
            cnt += 1
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += 1
            n -= n&(-n)
        return cnt


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += (n&1)
            n >>= 1
        return cnt