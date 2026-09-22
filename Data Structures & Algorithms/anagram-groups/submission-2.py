class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            anagrams[sorted_str] = [string]

        return anagrams.values()
        