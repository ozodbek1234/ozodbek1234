# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)


# #num = int(input("Enter a number:"))
# result = factorial(5)
# print(result)


# def sum_numbers(num):
#     result = 0
#     for i in range(1, num+1):
#         result += i
#     return result


# x = sum_numbers(10)
# print(x)

# def fibonacci(num):
#     result=[]
#     a,b=0,1
#     while a<num:
#         a,b=b,a+b

#         result.append(a)
#     return result

# x=fibonacci(100)
# print(x)

# double=lambda x:x*2
# #def double(x):
# #    return x*2
# my_list=[1,2,3,4,5,6,7,8,9]
# new_list=list(filter(lambda x:x%2==0,my_list))
# print(new_list)

# sonlar=list(range(1,11))
# kvadratlar=list(map(lambda x:x**2,sonlar))
# print(kvadratlar)
#!amaliyot_lambda_1
# x=lambda y:y*10
# print(x(10))

# x=lambda a,b:a+b
# print(x(10,20))

# import random as k

# sonlar = k.sample(range(0,1001), 10)
# kvadrat=list(map(lambda x:x**2,sonlar))
# toq_son=list(filter(lambda son:son%2==1,sonlar))
# print(kvadrat)
# print(toq_son)

# def sum_numbers(number):
#     """sum numbers from 1 to number"""
#     if number == 1:
#         return 1
#     else:
#         return number+sum_numbers(number-1)

# number=int(input("Enter a number:"))
# result = sum_numbers(number)
# print(result)

# def fibonacci(num):
#     x = []
#     a, b = 0, 1
#     while a < num:
#         a, b = b, a+b

#         x.append(a)

#     return x


# result = fibonacci(1000)
# print(result)
# import datetime

# x = datetime.datetime.now()
# print(x)
# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))
# lambda_factorial=lambda i:1 if i==0 else i*lambda_factorial(i-1)
# print(lambda_factorial(5))
# from collections import Counter
# CounterA=Counter(['a','b','b','c'])
# print(CounterA)

import random as r
x=r.randint(1,10)
print(x)
