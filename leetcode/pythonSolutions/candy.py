class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # candy = [1]*len(ratings)



        # for i in range(len(ratings)-1,0,-1):
            
        #     if ratings[i]>ratings[i-1] and candy[i]<=candy[i-1]:
        #         candy[i]+=1
        #     elif ratings[i]<ratings[i-1]:
        #         candy[i-1]+=candy[i]
            

        
        # for i in range(len(ratings)-1):
            
        #     if ratings[i]<ratings[i+1] and candy[i]>=candy[i+1]:

        #         candy[i+1]=candy[i]+1



        # return sum(candy)

        # The below code is from neetcode, which is far more efficient and readable.

        arr = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1]<ratings[i]:
                arr[i] = arr[i-1] + 1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                arr[i] = max(arr[i],arr[i+1]+1)

        return sum(arr)
