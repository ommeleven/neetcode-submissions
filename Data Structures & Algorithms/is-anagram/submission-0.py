class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        seen = set()
        for s_char in s:
            set.add(s_char)
        
        for t_char in t:
            set.remove(t_char)
        
        return set.isEmpty()
