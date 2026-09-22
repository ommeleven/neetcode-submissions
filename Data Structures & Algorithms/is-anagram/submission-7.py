class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        seen = {}
        for s_char in s:
            if s_char in seen:
                seen[s_char] += 1
                continue
            seen[s_char] = 1
        
        print(seen)
        for t_char in s:
            if t_char in seen:
                seen[t_char] -= 1
            
        if sum(seen.values()) != 0:
            return False
        return True
