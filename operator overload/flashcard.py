class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}: {self.meaning}"
    
flash = []
while True:
    word = input("Enter a word: ")
    meaning = input("Enter its meaning: ")

    flash.append(Flashcard(word, meaning))
    option = int(input("Do you want to add more flashcard? 0 if yes, 1 if no: "))
    if option == 1:
        break

print("\n<---Flashcards--->")
for i in flash:
    print(">", i)