class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            oldmax=maxi
            oldmin=mini
            maxi=max(x*oldmax,x*oldmin,x)
            mini=min(x*oldmax,x*oldmin,x)
            ans=max(ans,maxi)
        return ans