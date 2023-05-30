
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1),len(word2))
        ans = ""
        i = 0
        while i<l:
            ans+=word1[i]
            ans+=word2[i]
            i+=1

        if len(word2)>len(word1):
            ans+=word2[l:]
        else:
            ans+=word1[l:]

        return ans
