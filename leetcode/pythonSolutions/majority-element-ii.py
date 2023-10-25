class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
  
        n = len(nums)
        d = dict()
        for num in nums:
            d[num] = d.get(num,0)+1
        
        lst = []
        for key in d:
            if d[key]>n/3:
                lst.append(key)

        return lst
