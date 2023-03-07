class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = needle
        h = haystack
        np = 0
        hp = 0
        for i in range(0,len(h)):
            start = i
            if (len(h)-i)<(len(n)): 
                return -1
            for j in range(0,len(n)):
                print("this is", h[i], h[i+j], n[j])
                if h[i+j] == n[j]:
                    print(h[i+j], n[j], np)
                    np += 1
                else: 
                    np = 0
                    break 
                if np == len(n): return start
        return -1
