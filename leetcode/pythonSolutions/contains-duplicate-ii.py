class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        L = 0
        R = 0

        numSet = set()

        while R < len(nums):
            
            if R-L > k:
                numSet.remove(nums[L])
                L+=1

            if nums[R] in numSet:
                return True

            numSet.add(nums[R])
            
            R+=1
        
        return False

        

"""

Sharing the neetcode solution as it is better structured and more efficient

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k : 
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

"""
