class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedstr = ''.join(sorted(s))
            res[sortedstr].append(s)
        return list(res.values())