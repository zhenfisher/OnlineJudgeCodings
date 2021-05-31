class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n, res = len(nums), 0
        idx = [i for i in range(n)]
        idx.sort(key = lambda x: nums[x])
        left, right = [i for i in range(n)], [i for i in range(n)]
        st = []
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]:
                left[i] = left[st.pop()]
            st.append(i)
        st = []
        for i in range(n)[::-1]:
            while st and nums[st[-1]] >= nums[i]:
                right[i] = right[st.pop()]
            st.append(i)
        presums = [0]
        for i in range(n):
            presums.append(presums[-1]+nums[i])
        for i in idx:
            res = max(res, nums[i]*(presums[right[i]+1]-presums[left[i]]))
        return res%MOD