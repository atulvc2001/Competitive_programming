
class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(map(int, sorted(str(num), reverse = True)))
        print(num)
        ans = 0
        pos = 0
        for i in range(len(num)):
            ans += num[i] * 10**pos
            print(ans)
            if i%2!=0:
                pos+=1
                print("this is pos", pos)

        return ans
