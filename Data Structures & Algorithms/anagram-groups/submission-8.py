class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for i, s in enumerate(strs):
            text = "".join(sorted(s))
            hashmap[text] = hashmap.get(text, []) + [s]
        
        for key in hashmap:
            result.append(hashmap[key])

        return result