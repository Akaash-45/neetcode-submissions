class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            total=nums[l]+nums[r]
            if total==target:
                return [l+1,r+1]
            elif total<target:
                l+=1
            else:
                r-=1
        return []