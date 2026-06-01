# Problem: Design Add and Search Words Data Structure
# Category: Trie
# Time Complexity: O(n)
# Space Complexity: O(n)

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.end = True

    def search(self, word):

        def dfs(index, node):

            if index == len(word):
                return node.end

            char = word[index]

            if char == ".":

                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                return False

            if char not in node.children:
                return False

            return dfs(index + 1, node.children[char])

        return dfs(0, self.root)
