class Car:
    name = ""
    color = ""

    def Start(self):
        print("Starting the engine ")
my_car = Car()
my_car.name="BMW"
my_car.color="Black"
print(my_car.name)
print(my_car.color)
my_car.Start()