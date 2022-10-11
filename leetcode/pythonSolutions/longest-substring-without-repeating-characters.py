# My iteration of the solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = set()
        l = 0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[j] not in d:
                    d.add(s[j])
                    l = max(l,len(d))
                else:
                    d.clear()
                    break
        
        return l
