'''
Lucy Jones
M3 Lab
'''

# create vehicle class with a type attribute
class Vehicle():
    def __init__(self, type):
        self.type = type

# create automobile class with year, make, model, doors, and roof attributes
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# get inputs for the car object to be created
carYear = input('Enter car year: ')
carMake = input('Enter car make: ')
carModel = input('Enter car model: ')
carDoors = input('Enter number of doors: ')
# check for valid carDoors value
while carDoors != '2' and carDoors != '4':
    print('Error. Cars can only have 2 or 4 doors.')
    carDoors = input('Enter number of doors: ')
carRoof = input('Enter roof type (solid or sunroof): ').lower()
# check for valid carRoof value
while carRoof != 'solid' and carRoof != 'sunroof':
    print('Error. Roof type can only be solid or sunroof.')
    carRoof = input('Enter roof type (solid or sunroof): ').lower()

# create Automobile instance called 'car' with the inputs created
car = Automobile(carYear, carMake, carModel, carDoors, carRoof)

# print info about the car object
print(f'Vehicle type: {car.type}\nYear: {car.year}\nMake: {car.make}\nModel: {car.model}\nNumber of doors: {car.doors}\nRoof type: {car.roof}')