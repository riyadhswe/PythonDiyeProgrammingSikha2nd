class Car:
    name = ""
    color = ""

    def Start():
        print("Starting the engine ")


Car.name = "Axio"
Car.color = "Red"
print("Car Name : ",Car.name )
print("Car Colour : ",Car.color)
Car.Start()