class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.make+" "+self.model+" "+str(self.year)
        return long_name.title()

    def read_odometer(self):
        print("The car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElecticalCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battary_size=70
    def describe_battary(self):
        print("This car has a "+str(self.battary_size)+"-kWh battary.")


my_Tesla = ElecticalCar("tesla", "model s", 2016)
print(my_Tesla.get_descriptive_name())
my_Tesla.update_odometer(23500)
my_Tesla.increment_odometer(100)
my_Tesla.read_odometer()
my_Tesla.describe_battary()