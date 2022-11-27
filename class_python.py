# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("Ozodbek",22)
# # print(p1.name)
# # print(p1.age)
# print(p1)
#!You_Tube Teach_with_Tim example
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         #print(name)
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self,age):
#         self.age=age
# d=Dog("Sharik",34)
# d.set_age(30)
# print(d.get_age())

# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#     def get_grade(self):
#         return self.grade
# class Course:
#     def __init__(self,name,max_students):
#         self.name=name
#         self.max_students=max_students
#         self.students=[]
#     def add_student(self,studet):
#         if len(self.students)<self.max_students:
#             self.students.append(studet)
#             return True
#         return False
#     def get_average(self):
#         pass
# s1=Student("Ozodbek",22,95)
# s2=Student("Tim",19,75)
# s3=Student("Jill",20,85)

# course=Course("Science",2)
# course.add_student(s1)
# course.add_student(s2)
#! Python Crash Course example
# class Dog():
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attribbutes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(self.name.title() + " is now sitting.")

#     def roll_over(self):
#         print(self.name.title()+" roll over.")

# my_dog=Dog("tuzik",32)
# your_dog=Dog("sharik",34)
# print("My dog name is "+ my_dog.name.title()+".")
# print("My dog is "+str(my_dog.age)+" years old.")
# my_dog.sit()
# # my_dog.roll_over()
# print("\nYour dog's name is "+ your_dog.name.title()+".")
# print("Your dog is "+str(your_dog.age)+" years old.")
# your_dog.sit()
#! Restaurant
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print("Restaurant name is "+self.name.title()+".")

#     def open_restaurant(self):
#         print(self.name.title()+" restaurant is open.")


# restaurant_navoi = Restaurant("Sharqona", "National foods")
# print(restaurant_navoi.name+" is located in Navoi city.")
# print(restaurant_navoi.cuisine_type + " is very delicious.")
# restaurant_navoi.describe_restaurant()
# restaurant_navoi.open_restaurant()

#! PCC exmple_2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.make+" "+self.model+" "+str(self.year)
        return long_name.title()

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You ca not roll back an odometer.")

    def incremet_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")


my_used_car = Car("audi", "a4", 2016)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.incremet_odometer(100)
my_used_car.read_odometer()
