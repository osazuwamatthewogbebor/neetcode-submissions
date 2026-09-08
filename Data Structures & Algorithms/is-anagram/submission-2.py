from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        for key in Counter(s).keys():
            if Counter(s)[key] != Counter(t)[key]:
                return False

        return True
        