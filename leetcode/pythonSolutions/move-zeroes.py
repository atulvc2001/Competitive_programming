
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        no_z = nums.count(0)
        l = 0
        length = len(nums)
        print(nums)
        i = 0
        while l<length and i<length:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
                i+=1

            else: l+=1
