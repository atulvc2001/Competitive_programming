class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        ptr = l - 2

        if l<=2: return nums.reverse()
        
        while ptr>=0 and nums[ptr] >= nums[ptr + 1]:
            ptr -= 1

        if ptr == -1:
            return nums.reverse()
        
        for x in range(l-1,ptr,-1):
            if nums[x]>nums[ptr]:
                print("x: ", nums[x], "ptr: ", nums[ptr])
                nums[x],nums[ptr] = nums[ptr],nums[x]
                break
       
        nums[ptr+1:] = reversed(nums[ptr+1:])

        return nums
