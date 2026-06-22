class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append([n, i])
        
        return result