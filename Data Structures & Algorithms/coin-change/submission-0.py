class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]* (amount+1) for _ in range(n)]
        def f(ind,target):
            if target==0:
                return 0
            if ind==0:
                if target % coins[0]==0:
                    return target//coins[0]
                return float('inf')
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_pick=f(ind-1,target)
            pick=float('inf')
            if coins[ind]<=target:
                pick=1+f(ind,target-coins[ind])
            dp[ind][target]=min(pick,not_pick)
            return dp[ind][target]
        ans=f(n-1,amount)
        if ans ==float('inf'):
            return -1
        return ans 