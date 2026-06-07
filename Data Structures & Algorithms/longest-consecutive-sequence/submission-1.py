class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        options = set(nums)

        for n in options:
            if n - 1 in options:
                continue
            length = 1
            while n + length in options:
                length += 1
            max_length = max(max_length, length)
        
        return max_length
