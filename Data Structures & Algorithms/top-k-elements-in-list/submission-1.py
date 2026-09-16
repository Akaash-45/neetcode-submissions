class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        sorted_nums=sorted(freq,key=freq.get,reverse=True)
        return sorted_nums[:k]