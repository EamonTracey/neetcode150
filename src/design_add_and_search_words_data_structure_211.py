# Design a data structure that supports adding new words
# and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can
#   be matched later.
# - bool search(word) Returns true if there is any string in
#   the data structure that matches word or false otherwise. word
#   may contain dots '.' where dots can be matched with any letter.

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        for i, char in enumerate(word):
            if char == ".":
                return any(wd.search(word[i + 1:]) for wd in node.children.values())
            elif char not in node.children:
                return False
            node = node.children[char]
        return node.end
