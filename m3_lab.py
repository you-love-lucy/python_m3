'''Instructions
Complete the following steps:
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof'''

class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

carYear = input('Enter car year: ')
carMake = input('Enter car make: ')
carModel = input('Enter car model: ')
carDoors = input('Enter number of doors: ')
while carDoors != '2' and carDoors != '4':
    print('Error. Cars can only have 2 or 4 doors.')
    carDoors = input('Enter number of doors: ')
carRoof = input('Enter roof type (solid or sunroof): ').lower()
while carRoof != 'solid' and carRoof != 'sunroof':
    print('Error. Roof type can only be solid or sunroof.')
    carRoof = input('Enter roof type (solid or sunroof): ').lower()


car = Automobile(carYear, carMake, carModel, carDoors, carRoof)

print(f'Vehicle type: {car.type}\nYear: {car.year}\nMake: {car.make}\nModel: {car.model}\nNumber of doors: {car.doors}\nRoof type: {car.roof}')