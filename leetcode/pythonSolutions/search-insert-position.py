class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        print(l , r, "l", target)
        while l<=r:
            m =  (l+r)//2
            if target>nums[m]:
                l = m+1
                print(l, nums[m])
            elif target<nums[m]:
                r = m-1
                print(l, nums[m])
            elif target == nums[m]:
                return m

        return l
