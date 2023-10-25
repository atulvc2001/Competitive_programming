class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = dict()
        for num in nums:
            d[num] = d.get(num,0)+1

        maxnum = max(d.values())
        for key in d:
            if maxnum == d[key]:
                return key
