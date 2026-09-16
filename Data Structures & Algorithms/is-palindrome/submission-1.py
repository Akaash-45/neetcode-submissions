class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for ch in s:
            if ch.isalnum():
                arr.append(ch.lower())
        return arr==arr[::-1]