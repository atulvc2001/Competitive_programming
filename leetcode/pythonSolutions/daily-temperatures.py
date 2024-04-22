class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        monostack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while monostack and temperatures[monostack[-1]] <= temperatures[i]:
                monostack.pop()
            
            if monostack:
                ans[i] = monostack[-1] - i
            
            monostack.append(i)

        return ans
