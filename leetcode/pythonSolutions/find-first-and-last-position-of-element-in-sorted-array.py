class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        left,right = -1,-1
        while l<=r:
            m = (l+r)//2

            if target<nums[m]:
                r = m-1
                print("l:",l)
            elif target>nums[m]:
                l = m+1
                print(r)
            else:
                left = m
                if nums[m]==nums[m-1]:
                    r = m-1
                elif m == len(nums)-1 or nums[m]!=nums[m-1]:
                    break
        
        if left == -1: return [left,right]
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2 

            

            if target<nums[m]:
                r = m-1
            elif target>nums[m]:
                l = m+1
            else:
                right = m
                if m == len(nums)-1: break
                print("this is right", right)
                if nums[m]==nums[m+1]:
                    l = m+1
                    print("YO what fff",l)
                elif m == len(nums)-1 or nums[m]!=nums[m+1]:
                    print()
                    break

        return [left,right]    

"""
The above code is my solution, but I know it is utter garbage, hence I'm going to paste two cleaner solutions, one from neet code and the other from chatgpt

neetcode:
class solution:

    def searchRange(self, nums: List[int], target:int)->List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, True)
        return [left,right]
    
    def binSearch(self,nums,target, leftbias):
        
        l = 0
        r = len(nums)-1
        i = -1
        while l<=r:
            m = (l+r)//2

            if target<nums[m]:
                r = m-1
            elif target>nums[m]:
                l = m+1
            else:
                i = m
                if leftbias:
                    r = m-1
                else:
                    l = m + 1
        return i

chatGPT:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        left,right = -1,-1
        while l <= r:
            m = (l+r)//2

            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                left = m
                if m == 0 or nums[m]!=nums[m-1]:
                    break
                else:
                    r = m-1
        
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                right = m
                if m == len(nums)-1 or nums[m]!=nums[m+1]:
                    break
                else: 
                    l = m+1

        return [left,right]


"""
