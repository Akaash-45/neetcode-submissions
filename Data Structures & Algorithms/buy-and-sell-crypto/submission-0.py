class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        mprofit=0
        for price in prices:
            minp=min(minp,price)
            profit=price-minp
            mprofit=max(mprofit,profit)
        return mprofit
