ALPHABET_SIZE = 26

# the node in the tree structure
class Node:
    def __init__(self, character) -> None:
        self.character = character
        self.children = [None for _ in range(ALPHABET_SIZE)]
        self.leaf = False

class Trie:
    def __init__(self) -> None:
        # the root node is an empty node
        self.root = Node('*')
    
    # inserting an item takes O(M) time where M is the size of the word
    def insert(self, word):
        current = self.root
        for char in word:
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index] is not None:
                current = current.children[ascii_index]
            else:
                node = Node(char)
                current.children[ascii_index] = node
                current = node
        current.leaf = True
    
    def sort(self):
        return self.get_words_prefix('')
    
    def get_words_prefix(self, prefix):
        node = self.root
        words = []
        # we consider all the letters in the prefix
        for char in prefix:
            ascii_index = ord(char) - ord('a')
            if node.children[ascii_index] is None:
                return None
            node = node.children[ascii_index]
        
        # then we collect all the words starting with the same prefix
        self.collect(node, prefix, words)
        return words

    def collect(self, node, prefix, words):
        if node is None:
            return
        if node.leaf:
            words.append(prefix)
        for child in node.children:
            if child is None:
                continue
            child_character = child.character
            self.collect(child, prefix + child_character, words)
    
    def find(self, word):
        # if the tree is empty we return false
        if not self.root.children:
            return False
        current = self.root

        for char in word:
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index]:
                current = current.children[ascii_index]
            else:
                return False
        
        if current.leaf:
            return True
        
        return False

if __name__ == '__main__':
    trie = Trie()
    trie.insert('sea')
    trie.insert('seashell')
    trie.insert('seagull')
    trie.insert('bee')
    trie.insert('car')
    trie.insert('computer')

    print(trie.find('ca'))
    print(trie.find('sea'))
    print(trie.get_words_prefix('adam'))
    print(trie.get_words_prefix('sea'))
    print(trie.sort())