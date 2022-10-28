# thislist = ["apple", "banana", "cherry"]
# newlist=[]
# thislist.pop()
# print(thislist)
# for x in thislist:
#     print(x)
# for x in thislist:
#   if "a" in x:
#     newlist.append(x)
#     print(newlist)

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# cars.reverse()
# print(cars)
# cars=["Audi", "Tesla", "Mercedes", "AMG","Ferrari", "Bugatti", "Ford"]
# juft_sonlar=list(range(0,20,2))
# max_son=max(juft_sonlar)
# print(max_son)
# min_son=min(juft_sonlar)
# print(min_son)
# total=sum(juft_sonlar)
# print(total)
# my_cars=cars[:]
# print(my_cars)
# my_cars.append("Bmw")
# print(cars)
# print(my_cars)

# toys=("Teddy","Bear", "Snake", "Bee")
# print(toys[0])
# toys[1]="Bus"
# print(toys)
# import numbers
# import random
# numbers=[]
# for _ in range(10):numbers.append(random.randint(1,20))
# print(numbers)
# numbers.sort()
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
import random
numbers=[]
number_size=random.randint(10,15)
print(number_size)
for _ in range(number_size):
 numbers.append(random.randint(10,20))
print(numbers)
numbers.sort()
print(numbers)