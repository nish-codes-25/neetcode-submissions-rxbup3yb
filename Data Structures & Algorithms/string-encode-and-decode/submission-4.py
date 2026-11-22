class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            num, word = '', ''
            while s[i] != "#":
                num += s[i]
                i += 1

            num = int(num)
            for j in range(i+1, i+num+1):
                word += s[j]
            res.append(word)

            i = i + num + 1
        return res