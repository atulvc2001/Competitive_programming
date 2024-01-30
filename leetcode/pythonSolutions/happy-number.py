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
