class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for ch in s:
            if ch.isalnum():
                arr.append(ch.lower())
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l]!=arr[r]:
                return False
            l+=1
            r-=1
        return True