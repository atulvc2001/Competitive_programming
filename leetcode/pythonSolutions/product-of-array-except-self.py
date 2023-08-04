
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)
        res = []

        pre = 1
        for i in range(0,l):
            res.append(pre)
            pre *= nums[i]

        post = 1
        for i in range(l-1,-1,-1):
            res[i] = res[i]*post
            post *= nums[i]

        return res

        
