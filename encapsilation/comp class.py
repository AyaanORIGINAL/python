class Computer:
    def __init__(self):
        self.__maxprice = 1000
    
    def sell(self):
        print(f"Selling price: {self.__maxprice}")

    def setmaxprice(self, price):
        c.__maxprice = price
        
c = Computer()
c.sell()
c.setmaxprice(800)
c.sell()