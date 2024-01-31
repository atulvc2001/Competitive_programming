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

        
