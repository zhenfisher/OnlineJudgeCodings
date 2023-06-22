
# 2023.05.24-暑期-第三题-网络升级改造
# 题目描述

# 这天塔子哥在优化他以前做过的一个网络部署的项目，由于软件技术的提升，可以撤销部署网络中的某些节点，以简化网络并降低维护成本。但是，在撤销节点时，不能同时撤销原本直接相邻的两个节点。给定一个满二叉树结构的网络，每个节点上都标有一个数值，表示该节点的年度维护成本。现在要求撤销一些节点，使得可以节省最大的维护成本。

# 输入的网络以广度优先遍历的方式给出，每个节点都有一个非负整数值表示其年度维护成本。若某个节点不存在，则以00表示。每个数值的范围为 00 到 10001000。
# 输入描述

# 输入第一行为一个正整数NN，表示后面有NN个数值。其中1≤1≤N≤10000≤10000

# 输入第二行为NN个非负整数，表示网络节点每年的维护成本，按照满二叉树的广度优先遍历顺序给出。00 表示不存在该关联节点，00 只会存在于叶子节点上。
# 输出描述

# 输出能够节省的最大维护成本。
# 示例1

# 输入

# 7
# 5 3 5 0 6 0 1

# 输出

# 12

# 解释：

# 能够节省的最大维护成本为55 +66 + 11 = 1212。
# 示例2

# 输入

# 7
# 2 7 8 2 4 9 2

# 输出

# 19

# 解释：

# 能够节省的最大维护成本为 22 + 88 + 99 = 1919.
# 7
# 2 7 8 2 4 9 2

# Accepted 21.281688ms 3448KiB
# 19

from functools import *
n = int(input())
arr = list(map(int,input().split()))

@lru_cache(None)
def dfs(i,s):
    if i >= n: return 0
    if s == 1:
        return arr[i]+dfs(i*2+1,0)+dfs(i*2+2,0)
    else:
        return max(dfs(i*2+1,0),dfs(i*2+1,1))+max(dfs(i*2+2,0),dfs(i*2+2,1))

print(max(dfs(0,0),dfs(0,1)))
