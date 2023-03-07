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

# But this is not efficient, so the solution below is from neetcode

"""
for i in range(len(h)+1-len(n)):
    for j in range(len(n)):
        if h[i+j]!=n[j]:
            break
        if j == len(n)-1:
            return i
return -1

And a far more simpler solution is

for i in range(len(h)+1-len(n)):
    if h[i:i+len(n)] == needle:
        return i

which is stupidly more simpler

but there is an even more efficient solution using the KMP algorithm
"""
