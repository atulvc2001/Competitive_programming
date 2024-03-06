class Solution:

    def calculate(self, s: str) -> int:
        num, PreSign, stack=0, '+', []
        for c in s+'+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if PreSign=='+':
                    stack.append(num)
                elif PreSign == '-':
                    stack.append(-num)
                elif PreSign == '*':
                    stack.append(stack.pop()*num)
                elif PreSign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                PreSign=c
                num=0             
        return sum(stack)


"""
the below solution uses O(N) T.O and O(1) S.O
    
class Solution:
    def calculate(self, s: str) -> int:
        

        i = 0
         
        cur = prev = res = 0
        cur_operation = "+"

        while i < len(s):
            cur_char = s[i]

            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])

                    i+= 1
                
                i-= 1

                if cur_operation == "+":
                    res += cur
                    prev = cur

                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev*cur
                    prev = cur * prev
                else: 
                    res -= prev
                    res += int(prev/cur)

                    prev = int(prev/cur)
            
                cur = 0
            elif cur_char != " ":
                cur_operation = cur_char
            
            i+=1

        return res


"""
