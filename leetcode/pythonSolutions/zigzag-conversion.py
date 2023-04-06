class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        l = len(s)
        lst = [""]*numRows
        ind = numRows+1
        flag = False
        for i in range(0,l):
            if flag == True:
                ind += 1
            else: ind -= 1    
            lst[numRows - ind] = lst[numRows - ind]+s[i]
            print(lst[numRows - ind], numRows - ind, s[i])
            if ind == 1:
                flag = True
            if ind == numRows:
                flag = False

        return "".join(lst)

"""
This is a better solution from neetcode

def convert(self, s, numRows):
    if numRows == 1: return s

    res = ""
    for r in range(numRows):
        increment 2*(numRows-1)
        for i in range(r, len(s), increment):
            res+=s[i]                                               # This line only adds the letters at the index and only at it's increments
            if (r>0 and r<numRows-1 and i+increment-2*r<len(s)):
                res+=s[i+increment-2*r]                             # This line adds the letters at the index, the letters in between it's increments

    return res      


"""
