

class SetOfWords:
    def __init__(self):
        self.conjunto = set()
    
    def add(self, word):
        return self.conjunto.add(word.title())
    
    def delete(self, word):
        if word.title() in self.conjunto:
            self.conjunto.remove(word.title())
    
    def size(self):
        return len(self.conjunto)
    
s = SetOfWords()
s.add("Maria")
s.add("Manel")
s.add("MANEL")
s.add("manel")
print(s.size())