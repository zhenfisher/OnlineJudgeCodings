class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [0]*n
        for i, ss in enumerate(s):
            if i >= 1 and i-1-dp[i-1] >= 0 and ss == ')' and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1] + 2
                # print(i, dp[i])
                if i-2-dp[i-1] >= 0:
                    # print(i-2-dp[i-1], "exist")
                    dp[i] += dp[i-2-dp[i-1]]
                ans = max(ans, dp[i])
        # print(dp)
        return ans 