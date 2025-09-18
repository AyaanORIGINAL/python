class India():
    def capital(self):
        print("New Delhi is the capital of India")
        
    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a developing country")

class USA():
     def capital(self):
            print("Washington, D.C. is the capital of USA")

     def language(self):
            print("English is the primary language of USA")

     def type(self):
            print("USA is a developed country")

class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh")

    def language(self):
        print("Bengali is the primary language of Bangladesh")

    def type(self):
        print("Bangladesh is an underdeveloped country")
        
obj_ind = India()
obj_us = USA()
obj_bd = Bangladesh()

for country in (obj_ind, obj_us, obj_bd):
    country.capital()
    country.language()
    country.type()
    print()