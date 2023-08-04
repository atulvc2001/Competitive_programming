class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = []
        nums = sorted(nums1+nums2)
        l = 0
        r = len(nums)-1
        while l<r:
            print("this is",l,r)
            l+=1
            r-=1

        med = (nums[l]+nums[r])/2

        return med
