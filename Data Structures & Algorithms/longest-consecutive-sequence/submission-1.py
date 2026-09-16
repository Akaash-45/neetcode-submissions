class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        best=0
        for x in num_set:
            if x-1 in num_set:
                continue
            length=1
            while x+length in num_set:
                length+=1
            best=max(best,length)
        return best
