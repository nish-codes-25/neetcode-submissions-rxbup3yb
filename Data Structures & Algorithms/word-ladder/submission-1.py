class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque([[beginWord, 1]])
        while q:
                word, length = q.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        next_word = word[:i]+c+word[i+1:]
                        if next_word in wordList:
                            wordList.remove(next_word)
                            q.append([next_word, length+1])
        return 0