#class Solution:
    #def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #
        #result = 0
        #def isAnswer(val):
            #arr = [math.ceil(x / val) for x in piles]
            ## print("this is the arr ", sum(arr), " and this is val", val, h)
            #return sum(arr) <= h
        #
        #r = max(piles)
        ## rng = list(range(1,end+1))
        #l = 1
        #while l<=r:
            #k = (l+r)//2
            ## print(k,l,r)
            #if isAnswer(k):
                #result = k
                #r = k - 1
            #else:
                #l = k + 1
        #return result

# The above is my solution and the below is by neetcode

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = r

        while l <= r :
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
