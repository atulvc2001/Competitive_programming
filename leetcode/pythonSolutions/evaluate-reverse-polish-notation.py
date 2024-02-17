class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        if len(tokens) < 3:
            return int(tokens[0])
        for i in tokens:
            if not i.isdigit():
                # print("this is the stack in for loop ",stack)
                if i == "/":
                    lastNum = int(stack.pop())
                    secondLastNum = int(stack.pop())
                    if secondLastNum / lastNum < 0:
                        ans = math.ceil(secondLastNum / lastNum)
                    else:
                        ans = secondLastNum // lastNum
                    stack.append(ans)
                    continue
                elif i == "*":
                    stack.append(int(stack.pop())*int(stack.pop()))
                    continue
                elif i == "+":
                    stack.append(int(stack.pop())+int(stack.pop()))
                    continue
                elif i == "-":
                    lastNum = int(stack.pop())
                    secondLastNum = int(stack.pop())
                    ans = secondLastNum - lastNum
                    stack.append(ans)
                    continue
            stack.append(i)

        # print(stack)
        return stack[0]
