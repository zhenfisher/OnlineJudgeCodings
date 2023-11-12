
# 2023.09.09-美团-第五题-塔子哥的子数组权值和
# 题目描述

# 塔子哥有一个长度为 nn 的数组 aa 。

# 他对一个数组的权值定义为，这个数组中两个不同的不同下标 i,j(0≤i<j<n)i,j(0≤i<j<n) ，所有 ai xor ajai​ xor aj​ 的和。
# 即 ∑i=0n−2∑j=i+1n−1ai xor aji=0∑n−2​j=i+1∑n−1​ai​ xor aj​ 。

# 现在塔子哥想要问你，这个数组的所有连续子数组的权值之和是多少。
# 输入描述

# 第一行，一个整数 n(1≤n≤105)n(1≤n≤105)，表示数组的长度。
# 第二行，nn 个整数，第 ii 个整数为 ai(1≤ai≤109)ai​(1≤ai​≤109) 。
# 输出描述

# 一个整数，表示所有子数组的权值之和，答案对 109+7109+7 取模
# 样例

# 输入

# 3
# 1 2 3

# 输出

# 10

# 说明

# 对于子数组 a[1,2]a[1,2] 来说，权值为 33
# 对于子数组 a[2,3]a[2,3] 来说，权值为 11
# 对于子数组 a[1,2,3]a[1,2,3] 来说，权值为 66
# 3+1=6=103+1=6=10


n = int(input())
arr = list(map(int,input().split()))
MOD = 10**9+7
ans = 0
base = 1
for _ in range(32):
    cc = [0]*2 
    for i in range(n):
        a = arr[i]&1
        arr[i] >>= 1 
        ans += cc[a^1]*(n-i)*base  
        ans %= MOD 
        cc[a] += i+1
        cc[a] %= MOD 
    base <<= 1
print(ans)
