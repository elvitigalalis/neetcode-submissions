class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        res = 0

        for i in range(1, len(height) - 1):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        
        print(leftMax)
        for i in range(len(height) - 2, 0, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        
        print(rightMax)
        for i in range(1, len(height) - 1):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if water > 0:
                res += water
        
        return res