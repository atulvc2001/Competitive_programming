
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        
        s_list = sorted(points,key=lambda x:x[0])
        balloons = len(s_list)
        i = 1
        r = s_list[0][1]
        l = s_list[0][0]
        # l = s_list[j][0]
        print(s_list)

        while i<len(s_list):
            
            if r<s_list[i][0]:
                l = s_list[i][0]
                r = s_list[i][1]
                i+=1
                continue

            l = max(l,s_list[i][0])
            r = min(r,s_list[i][1])
            i+=1
            balloons-=1


        return balloons

"""
if you want to calculate the number arrows directly, use the below code
        if not points: return 0
        points.sort()
        prev = points[0]
        total = 1
        for s,e in points[1:]:
            if s>prev[1]:
                total += 1
                prev = [s,e]
            else:
                prev[1] = min(prev[1],e)

        return total
"""
