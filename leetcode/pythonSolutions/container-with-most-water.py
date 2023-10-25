class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        prod = 0
        while l<r:
            minlen = min(height[r],height[l])
            if prod < abs(r-l)*minlen:
                prod = abs(r-l)*minlen
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return prod
