class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(t)
        for i , temp in enumerate (t):
            while stack and temp > t[stack[-1]]:
                prev=stack.pop()
                ans[prev]=i-prev
            stack.append(i)
        return ans
