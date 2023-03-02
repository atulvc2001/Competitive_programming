class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend==0): return 0
        if((dividend == -(2**31)) and (divisor == -1)): return ((2**31)-1)
        a = abs(dividend)
        b = abs(divisor)
        q=0
        while a-b>=0:
            c = 0
            
            while(a-b*(2**c)>=0):
                c+=1
                print("This is c -->",c)
            q += 2**(c-1)
            a = a-b*(2**(c-1))
            print("jj",a)
            
        print("--->", q)

        if (dividend>0) == (divisor>0): 
            print("Trueeee")
            return q

        else:
            print("djdjdj",-q)
            return -q
