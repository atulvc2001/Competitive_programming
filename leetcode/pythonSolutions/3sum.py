class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        p = 0
        l = 1
        r = len(nums)-1
        d = dict()
        lst = []
        nums.sort()

        while p<len(nums)-2:
            l = p+1
            r = len(nums)-1 
            while l<r:
                if nums[p] == -(nums[l]+nums[r]):
                    if [nums[p],nums[l],nums[r]] not in lst: lst.append([nums[p],nums[l],nums[r]])                  
                    else: 
                        l+=1
                        r-=1
                        continue
                    l+=1
                    r-=1
                elif -(nums[p])<nums[l]+nums[r]:
                    r-=1
                else:
                    l+=1

            p+=1

        return lst

    # the above solution is mine, the below one is an optimized solution
