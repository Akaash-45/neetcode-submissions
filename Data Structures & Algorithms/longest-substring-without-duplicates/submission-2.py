class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_seen={}
        l=0
        ans=0
        for r in  range(len(s)):
            if s[r] in l_seen:
                l=max(l,l_seen[s[r]]+1)
            l_seen[s[r]]=r
            ans=max(ans,r-l+1)
        return ans