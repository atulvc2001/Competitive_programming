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
