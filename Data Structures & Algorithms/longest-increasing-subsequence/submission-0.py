class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[ind][prev + 1]
        # Stores the LIS length for a given (ind, prev) state
        dp = [[-1] * (n + 1) for _ in range(n)]

        def f(ind, prev):
            # No elements left to process
            if ind == n:
                return 0

            # If this state was already calculated, reuse it
            if dp[ind][prev + 1] != -1:
                return dp[ind][prev + 1]

            # Choice 1: Don't take nums[ind]
            notTake = f(ind + 1, prev)

            # Choice 2: Take nums[ind] if it maintains increasing order
            take = 0

            if prev == -1 or nums[ind] > nums[prev]:
                take = 1 + f(ind + 1, ind)

            # Store the best of taking and not taking
            dp[ind][prev + 1] = max(take, notTake)

            return dp[ind][prev + 1]

        # Start from index 0 with no previous element
        return f(0, -1)