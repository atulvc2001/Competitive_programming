class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        l = 0
        r = len(s)-1
        lst = list(s)

        while l<r:
            print("this is the orig:   ",lst[l],lst[r])
            if lst[l] not in vow:
                l+=1
            if lst[r] not in vow:
                r-=1
            if lst[l] in vow and lst[r] in vow:
                print("Before swap:    ",lst[l],lst[r])
                lst[l],lst[r] = lst[r],lst[l]
                
                l+=1
                r-=1 

        return "".join(lst)
