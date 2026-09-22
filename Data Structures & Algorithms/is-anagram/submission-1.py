class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        seen = set()
        for s_char in s:
            seen.add(s_char)
        
        for t_char in t:
            seen.remove(t_char)
        
        return seen.isEmpty()
