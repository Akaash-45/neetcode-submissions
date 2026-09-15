class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        for x in s:
            a[x]=a.get(x,0)+1
        for x in t:
            a[x]=a.get(x,0)-1
        return all(a[x]==0 for x in a)
