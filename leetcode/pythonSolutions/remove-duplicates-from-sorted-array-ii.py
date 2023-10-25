class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        d = dict()
        for i in nums:
            d[i] = d.get(i,0)+1

        for k,v in d.items():
            if v>2:
                c = v
                while c>2:
                    nums.remove(k)
                    nums.append('_')
                    c-=1
        countofnum = sum(1 for num in nums if isinstance(num,int))
        return countofnum
