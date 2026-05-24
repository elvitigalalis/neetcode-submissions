class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        for c in t:
            if count[c] <= 0:
                return False
            else:
                count[c] -= 1
                if count[c] == 0:
                    del count[c]
        return len(count) == 0
