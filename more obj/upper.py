class IOString:
    def __init__(self):
        self.str1 = ''

    def get_string(self):
        self.str1 = input("Enter a string: ")

    def print_upper(self):
        print("Uppercase: ", self.str1.upper())

    def print_reverse(self):
        print("reversed: ", self.str1[::-1])

    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in self.str1:
            if char in vowels:
                count +=1
        print("Number of vowels: ", count)

    def count_consonants(self):
        vowels = 'aeiouAEIOU'
        count = 0
        for char in self.str1:
            if char not in vowels:
                count +=1
        print("Number of consonants: ", count)

s1 = IOString()
s1.get_string()
s1.print_upper()
s1.print_reverse()
s1.count_vowels()
s1.count_consonants()
