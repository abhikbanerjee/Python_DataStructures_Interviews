from typing import List

# Evaluate a Reverse Polish Notation - LC 150
def evalRPN(tokens: List[str]) -> int:
        if not tokens:
            return -1
        st_tokens = []
        for token in tokens:
            if token=="+" or token=="-" or token=="/" or token=="*":
                # pop the last 2 tokens from stack apply the operation and push the result back
                if not st_tokens:
                    # seems to be an error
                    return -1
                operand1 = st_tokens.pop()
                operand2 = st_tokens.pop()
                result = -1
                if token=="+":
                    result = operand2 + operand1
                if token=="-":
                    result = operand2 - operand1
                if token=="*":
                    result = operand2 * operand1
                if token=="/":
                    result = operand2//operand1 if abs(operand2)>abs(operand1) else operand1//operand2
                st_tokens.append(result)
            else:
                # append to the stack
                st_tokens.append(int(token))
        return st_tokens[-1]


li1 = ["4","13","5","/","+"]
li2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


# print(evalRPN(li1))
print(evalRPN(li2))