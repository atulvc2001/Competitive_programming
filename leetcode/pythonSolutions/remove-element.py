class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        c = 0
        for i in range(0,l):
            if nums[i] != val:
                nums[c] = nums[i]
                c+=1
        return c
