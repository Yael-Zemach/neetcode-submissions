class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i,value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                num = stack.pop()
                result[num[1]] = i - num[1]
            stack.append((value, i))
        return result
            


