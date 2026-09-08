from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        s_hash = Counter(s)
        t_hash = Counter(t)

        for key in s_hash.keys():
            if s_hash[key] != t_hash[key]:
                return False

        return True
        