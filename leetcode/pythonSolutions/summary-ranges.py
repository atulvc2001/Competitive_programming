# the commented solution is the one I came up with that is not efficiently structured
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
        
#         op = []
#         if not nums: return op
        
#         s = 0
#         e = 0

#         if len(nums) == 1:
#             op.append(f"{nums[0]}")
#             return op

#         for i in range(0, len(nums)-1):
#             # print(i, nums[i])
#             if nums[i] + 1 != nums[i+1]:
#                 e = i
#                 if s == e:
#                     op.append(f"{nums[s]}")
#                 else:
#                     op.append(f"{nums[s]}->{nums[e]}") 
#                 s = i + 1
#             e = i + 1

#         if s == e:
#             op.append(f"{nums[s]}")
#         else:
#             op.append(f"{nums[s]}->{nums[e]}") 
#         return op


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        op = []
        if not nums:
            return op
        
        s = e = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if s == e:
                    op.append(str(nums[s]))
                else:
                    op.append(f"{nums[s]}->{nums[e]}") 
                s = e = i
            else:
                e = i

        if s == e:
            op.append(str(nums[s]))
        else:
            op.append(f"{nums[s]}->{nums[e]}") 

        return op
