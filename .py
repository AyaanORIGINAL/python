def make_cakes(flour, sugar):
    flour_needed = 100  
    sugar_needed = 50   
    cake_count = 0      

    while True:
        if flour < flour_needed or sugar < sugar_needed:
            break 

        flour -= flour_needed
        sugar -= sugar_needed
        cake_count += 1

    flour_left = flour
    sugar_left = sugar

    return cake_count, flour_left, sugar_left


flour = int(input("How many units of flour? "))
sugar = int(input("How many units of sugar? "))
cakes, flour_left, sugar_left = make_cakes(flour, sugar)

print("Cakes made:", cakes)
print("Flour left:", flour_left)
print("Sugar left:", sugar_left)
