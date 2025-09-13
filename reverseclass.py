class Reverse:
    def __init__(self, word=""): 
        self.word = word

    def reversed_string(self):
        return self.word[::-1]  

word = input("Enter a word: ")  
rev = Reverse(word)             
print("Reversed string:", rev.reversed_string())
