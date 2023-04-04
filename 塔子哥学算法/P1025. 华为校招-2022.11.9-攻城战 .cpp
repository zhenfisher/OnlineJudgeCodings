// 题目解析以及代码

// 关注公众号:塔子哥学算法，搜索“P1025”即可得到对应题解
// 攻城战
// 题目内容

// 一支攻城部队， 有若干种大炮各座， 以及数量有限的火药，每种大炮的威力不尽相同，且在每次开火之前都需要一定时间填充火药， 请你帮助指挥官在给定的时间结束之前或者火药存量耗尽之前给予城池最大的打击。

// 约束：

//     大炮每次开火的威力一样；
//     火药剩余量不小于大炮的消耗量，该大炮才能开火；
//     填充火药之外的时间忽略不计；
//     不同种大炮可以同时开火。

// 输入描述

// 第一行，整数 NN ， MM ， TT ， NN 表示大炮种类个数， MM 表示火药数量， TT 表示攻城时间，$1 \leq N,M,T \leq 1000。

// 接下来 NN 行，每一行三个整数 AA ， BB ， CC 。分别表示大炮的威力，大炮每次攻击消耗的火药量，大炮每次攻击填充火药的时间，0\leq A,B,C \leq 100000。
// 输出描述

// 输出在给定的时间结束之前或者火药存量耗尽之前给予城池最大的打击。
// 样例
// 样例一：

// 输入

// 3 100 20
// 10 8 5
// 5 2 1
// 20 25 8

// 输出

// 160

// 样例解释

// 总共有 33 种大炮，火药存量 100100 ， 攻城时间 2020 ;

// 第 11 种大炮威力 1010 ，每次攻击消耗火药 88 ，每次攻击填充火药时间 55 ；

// 第 22 种大炮威力 55 ，每次攻击消耗火药 22 ，每次攻击填充火药时间 11 ；

// 第 33 种大炮威力 2020 ，每次攻击消耗火药 2525 ，每次攻击填充火药时间 88 ；
// 样例二：

// 输入

// 2 10 10
// 1 1 1
// 2 2 2

// 输出

// 10

// 样例解释

// 总共有 22 种大炮，火药存量 1010 ，攻城时间 1010 ；

// 第 11 种大炮威力 11 ，每次攻击消耗火药 11 ，每次攻击填充火药时间 11 ；

// 第 22 种大炮威力 22 ，每次攻击消耗火药 22 ，每次攻击填充火药时间 22 ；

#include <iostream>
using namespace std;
int a[1005],b[1005],c[1005];
int dp[10004];
int main()
{
    int n,m,T;
    cin>>n>>m>>T;
    for (int i=0;i<n;i++)
        cin>>a[i]>>b[i]>>c[i];
    for (int i=0;i<n;i++)
    {
        for (int j=m;j>=0;j--)
        {
            int mx=min((m-j)/b[i],T/c[i]);
            for (int k=1;k<=mx;k++)
                dp[j+k*b[i]]=max(dp[j+k*b[i]],dp[j]+k*a[i]);
        }
    }
    int ans=0;
    for (int i=0;i<=m;i++)
        ans=max(ans,dp[i]);
    cout<<ans<<endl;
    return 0;
}