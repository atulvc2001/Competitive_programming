
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        print(matrix)
        length = len(matrix[0])
        l = 0
        r = len(matrix)-1
        flag = False
        while l<=r:
            i = (l+r)//2
            if target<=matrix[i][length-1]:
                if target>=matrix[i][0]:
                    if target in matrix[i]:
                        return not flag
                    else:
                        return flag
                else:
                    r = i-1
            else:
                l = i+1
        return flag

