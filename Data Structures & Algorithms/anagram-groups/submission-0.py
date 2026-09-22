class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        for string in strs:
            if sorted(string) in anagrams:
                anagrams[sorted(string)].append(string)
            anagrams[sorted(string)] = [string]

        return anagrams.values()
        