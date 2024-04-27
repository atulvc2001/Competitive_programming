# My iteration of the solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        tally = dict()
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in tally and tally[s[r]] >= l:
                l = tally[s[r]] + 1
            length = max(length, r - l + 1)
            tally[s[r]] = r
        return length
