class TriesNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.lastLeaf = False #true for the last leaf
 
    def addChild(self, TrieNode):
        self.children.append(TrieNode)
 
class Tries:
    def __init__(self): #constructor
        self.root = TriesNode(None)
 
    def insert(self, key):
        currentLetter = self.root
        length = len(key)
 
        for i in range(length):
            nextLetter = TriesNode(key[i])
            currentLetter.addChild(nextLetter)
            currentLetter = nextLetter
 
        currentLetter.lastLeaf = True
 
    def search(self, text):
        currentLetter = self.root
        for i in range(len(text)):
            for j in range(len(currentLetter.children)):
                if (text[i] == currentLetter.children[j].letter):
                    print(currentLetter.children[j].letter, "found at index", i)
                    currentLetter = currentLetter.children[j]
                    break
                else:
                    currentLetter = self.root
            if currentLetter.lastLeaf == True:
                return "Word exist"
        return "Word does not exist"
 
# driver
def main():
    key = ["fun"]
    text = "algorithmisfun"
 
    t = Tries()
 
    t.insert(key[0])
    print(t.search(text))
 
if __name__ == "__main__":
    main()
