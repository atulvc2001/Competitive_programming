class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def helper(word):
            output,lookup = [],{}
            i=1
            for l in word:
                if l not in lookup:
                    lookup[l] = i
                    i += 1
                output.append(lookup[l])
            return output
        
        return helper(s) == helper(t)
