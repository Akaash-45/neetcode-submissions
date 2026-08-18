class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n=len(costs)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1):
            one=costs[i]+dp[i+1]
            two=costs[i]+dp[i+2]
            dp[i]=min(one,two)
        return min(dp[0],dp[1])