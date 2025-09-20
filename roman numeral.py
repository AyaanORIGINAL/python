class RomanNumeral:
    def __init__(self, number: int):
        self.number = number
        self.value = self.int_to_roman()

    def int_to_roman(self) -> str:
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        num = self.number
        result = ""

        
        for value in sorted(roman_numerals.keys(), reverse=True):
            while num >= value:
                result += roman_numerals[value]
                num -= value

        return result

num = int(input("Enter a number (1 - 3999): "))

if 1 <= num <= 3999:
    converter = RomanNumeral(num)
    print("Roman numeral:", converter.value)
else:
    print("Enter a number between 1 and 3999.")
