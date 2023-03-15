class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 3,2
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        for i in range(n-3):
            temp = a
            print(a,b)
            a = a + b
            b = temp

        return a


"""

The following code is a much more simplified version of the above code, courtesy of neetcode

one,two = 1,1

for i in range(n-1):
    temp = one 
    one = one + two
    two = temp

return one

Some might say it's literally the same code, but it's not and one might ask why. Well, the first code is the result of my brain churning and churning and finally producing an answer after finally grasping this simple concept, whereas the other one get's straight to the answer. 

"""
