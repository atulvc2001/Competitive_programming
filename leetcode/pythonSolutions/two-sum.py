class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        
        for i in range(0,len(self.nums)-1):
            for j in range(i+1,len(self.nums)):
                if (self.nums[i] + self.nums[j]) == self.target:
                    return [i,j]
            
