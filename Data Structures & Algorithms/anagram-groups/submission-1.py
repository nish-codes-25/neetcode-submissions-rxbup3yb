class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     sortedstr = ''.join(sorted(s))
        #     res[sortedstr].append(s)
        # return list(res.values())
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for _ in s:
                count[ord(_)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())