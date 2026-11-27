class TreeNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            node = node.children[ch]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        print(word)
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.endOfWord
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True