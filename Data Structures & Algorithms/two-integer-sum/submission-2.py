class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[(nums[i],i) for i in range(len(nums))]
        arr.sort()
        l=0
        r=len(nums)-1
        while l<r:
            x=arr[l][0]+arr[r][0]
            if x==target:
                return sorted([arr[l][1],arr[r][1]])
            elif x>target:
                r-=1
            else :
                l+=1
        return []