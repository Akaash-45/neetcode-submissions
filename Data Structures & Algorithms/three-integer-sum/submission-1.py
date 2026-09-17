class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        for i in range(n):
            seen=set()
            for j in range(i+1,n):
                need=-nums[i]-nums[j]
                if need in seen:
                    triplet=tuple(sorted([nums[i],nums[j],need]))
                    ans.add(triplet)
                seen.add(nums[j])
        return [list(x) for x in ans]