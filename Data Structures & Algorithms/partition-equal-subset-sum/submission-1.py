class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        n=len(nums)
        dp=[[-1]*(target+1) for _ in range(n)]
        def f(ind,target):
            if target==0:
                return True
            if ind==n:
                return False
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_take=f(ind+1,target)
            take=False
            if nums[ind]<=target:
                take=f(ind+1,target-nums[ind])
            dp[ind][target]=take or not_take
            return dp[ind][target]
        return f(0,target)