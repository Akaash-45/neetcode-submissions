class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(arr):
            n=len(arr)
            dp=[0]*n
            dp[0]=arr[0]
            for i in range(1,n):
                not_pick=dp[i-1]
                pick=arr[i]
                if n>1:
                    pick+=dp[i-2]
                dp[i]=max(pick,not_pick)
            return dp[n-1]
        case1=solve(nums[1:])
        case2=solve(nums[:-1])

        return max(case1,case2)

