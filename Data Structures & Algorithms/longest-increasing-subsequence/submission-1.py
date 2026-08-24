class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def f(ind, prev):
            if ind == n:
                return 0
            if dp[ind][prev + 1] != -1:
                return dp[ind][prev + 1]
            notTake = f(ind + 1, prev)
            take = 0
            if prev == -1 or nums[ind] > nums[prev]:
                take = 1 + f(ind + 1, ind)
            dp[ind][prev + 1] = max(take, notTake)
            return dp[ind][prev + 1]
        return f(0, -1)