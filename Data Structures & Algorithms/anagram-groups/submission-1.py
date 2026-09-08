from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_map = {}

        for i in strs:
            key = tuple(sorted(Counter(i).items()))

            counter_map.setdefault(key, []).append(i)

        
        return list(counter_map.values())