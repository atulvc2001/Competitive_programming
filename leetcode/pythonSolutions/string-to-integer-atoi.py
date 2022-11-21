class Solution:
    def myAtoi(self, s: str) -> int:
        str = s.strip()
        
        if not str:
            return 0
        neg = False
        out = 0
        
        if str[0] == '-':
            neg = True
        elif str[0] == '+':
            neg = False
        elif not str[0].isnumeric():
            return 0
        else:
            out = ord(str[0]) - ord("0")
        
        for i in range(1,len(str)):
            if str[i].isnumeric():
                out = out*10 + (ord(str[i]) - ord("0"))
                if not neg and out>=2147483647:
                    return 2147483647
                if neg and out>=2147483648:
                    return -2147483648
            else: 
                break
        if not neg:
            return out
        elif neg:
            return -out
                
        
