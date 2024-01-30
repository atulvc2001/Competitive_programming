class Solution:
    def isHappy(self, n: int) -> bool:
        
        hash_set = set()
        sum = n
        while sum!=0:
            
            if sum not in hash_set:
                n = sum
                hash_set.add(n)
            else: return False
            
            if n == 1:
                return True
            sum = 0
            while n!=0:
                d = n%10
                sum += d*d
                n = n//10

        return False

'''
    class Solution:
        def isHappy(self, n: int) -> bool:
            visit = set()

            while n not in visit:
                visit.add(n)
                n = self.sumOfSquares(n)

                if n == 1:
                    return True

            return False

        def sumOfSquares(self, n: int) -> int:
            output = 0
            
            while n: 
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n//10
            return output


 # the above, better structured answer is from neetcode 










'''
