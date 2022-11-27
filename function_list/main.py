def bahola(ismlar):
    """talabalarni baholaydigan funksiya"""


#     lugat = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism.title()}ning bahosini kiriting:")
#         lugat[ism] = int(baho)
#     return lugat
#
#
# talabalar = ['hasan', 'husan', 'ali', 'vali']
# baholar = bahola(talabalar[:])
#
# print(baholar)
# print(talabalar)
# def hisobla(son):
#     """Yigindini hisoblaydigan funksiya"""
#     x_list = []
#     for x in range(1, son + 1):
#         x_list.append(x)
#
#     return sum(x_list)
#
#
# result = hisobla(10)
# print(result)
# def addition(num):
#     if num:
#         return num+addition(num-1)
#     else:
#         return 0
# res=addition(10)
# print(res)
# def calculation(a, b):
#     return print(a + b, a - b)
#
#
# calculation(40, 10)
# def generate_numbers(a, b):
#
#     """generate numbers from a to b step=2"""
#     x=list(range(a,b,2))
#     return x
#
#
# result=generate_numbers(4, 30)
# print(result)
# def factorial(num):
#     """calculate n factorial"""
#     if num == 1:
#         return 1
#     else:
#         return (num * factorial(num - 1))
#
#
# n=int(input("Enter a number:"))
# result = factorial(n)
# print("The factorial of", n, "is", result)

# def multiple(*numbers):
#     result = 1
#     for x in numbers:
#         result *= x
#     return result
#
#
# result_2 = multiple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result_2)

# def info_students(ism, familiya, **boshqa_malumotlar):
#     boshqa_malumotlar['ism'] = ism
#     boshqa_malumotlar['familiya'] = familiya
#     return boshqa_malumotlar
#
#
# student_1 = info_students("Ozodbek", "Toshpulatov", t_yil=2000, yosh=22, learn_languages="English,Russian",
#                           study="Navoi State University of Mining and Texnology")
# student_2 = info_students("Asilbek", "Murtazayev", t_yil=2001, yosh=21, profission="mathematician",
#                           study="Navoi State Pedagogical institute")
#
# for x, y in student_1.items():
#     print(x, y)

def build_profile(f_name, l_name, **user_info):
    x_frofile = {}
    """Build a dictionary containing everything we know about a user."""

    x_frofile['first_name'] = f_name
    x_frofile['last_name'] = l_name
    for key, value in user_info.items():
        x_frofile[key] = value
    return x_frofile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
