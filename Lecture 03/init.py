class Car:
    def __init__(self,n,c):
        self.name = n
        self.color = c

    def start(self):
        print("Name  :", self.name)
        print("Color :", self.color)
        print("======================")

my_car1 = Car("Corolla","White")
my_car1.start()
my_car1 = Car("Premo","Black")
my_car1.start()
my_car1 = Car("Allion","Blue")
my_car1.start()