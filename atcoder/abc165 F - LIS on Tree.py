import os,sys, threading
from random import randint, shuffle
from io import BytesIO, IOBase

from collections import defaultdict,deque,Counter
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop, heapify
from functools import lru_cache, reduce
from itertools import accumulate, permutations
import math, copy


# sys.setrecursionlimit(2**20)
# threading.stack_size(2**20)
sys.setrecursionlimit(0x0FFFFFFF)
threading.stack_size(0x08000000)

# resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])


# Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

MOD = 998244353  
from math import * 


def main():
    # def quickmul(a, p):
    #     res = 1
    #     while p:
    #         if p&1:
    #             res = (res*a)%MOD
    #         p >>= 1
    #         a = (a*a)%MOD
    #     return res 

    # def query(tree, x):
    #     s = 0
    #     while x:
    #         s = (tree[x]+s)%MOD
    #         x -= x&-x 
    #     return s 
    # def update(tree, x, v):
    #     while x < len(tree):
    #         tree[x] = (tree[x]+v)%MOD
    #         x += x&-x 
    #     return 

    def solve():
        n = int(input())
        # s = list(map(int, list(input())))
        arr = list(map(int, input().split()))
        g = defaultdict(list)
        ans = [-1]*n 
        for _ in range(n-1):
            u, v = list(map(int, input().split()))
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        def _bisect_left(xs, val, func = lambda x: x):
            if not xs:
                return 0
            lo, hi = 0, len(xs)-1
            while lo <= hi:
                mid = (lo+hi)//2
                if func(xs[mid]) >= val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo 

        def dfs(cur, parent, st):
            last = False 
            pre = -1
            m = len(st)
            v = arr[cur]
            sz = _bisect_left(st, v, func = lambda x: arr[x])
            
            if sz == m:
                last = True 
                st.append(cur)
            else:
                pre = st[sz]
                st[sz] = cur
            ans[cur] = len(st)
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(nxt, cur, st)
            if last:
                st.pop()
            else:
                st[sz] = pre 
            return
        dfs(0,0,[])
        for i in range(n):
            print(ans[i])
        return   



    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for i in range(t):
        # n, k = list(map(int, input().split())) 
        solve()
        # print(solve())
        # if solve():
        #     print("YA")   
        # else:
        #     print("TIDAK")
        # print(solve())
        # n = int(input())
        # arr = list(map(int, input().split()))     
        # if solve(n, m, k):
        #     print("YES")
        # else:
        #     print("NO")


    # debug(ans)


if __name__ == "__main__":
    # main()
    threading.Thread(target=main).start()


