class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            elif n<0:
                return 1/helper(x,-n)
            elif n%2==0:
                half_pow = helper(x,n//2)
                return half_pow*half_pow
            elif n%2!=0:
                half_pow = helper(x,n//2)
                return x*half_pow*half_pow
            

        return helper(x,n) if x != 0 else 0
