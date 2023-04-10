class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''.join(c for c in s if c.isalnum())
        print(new_s)
        lowstr = new_s.lower()
        print(lowstr)
        if not lowstr: return True
        l,r = 0,len(lowstr)-1
        while l<=r:
            if lowstr[l] != lowstr[r]:
                return False
            l+=1
            r-=1

        return True
