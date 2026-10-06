import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oprtn_dict = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        stack = []
        for ch in tokens:
            if ch not in oprtn_dict:
                stack.append(int(ch))
            else:
                b=stack.pop()
                a=stack.pop()
                res = int(oprtn_dict[ch](a,b))
                stack.append(res)
             
        return stack.pop()




            

        

