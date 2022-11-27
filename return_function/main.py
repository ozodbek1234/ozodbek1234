# def get_formatted_fullname(firstname, lastname, middlename=''):
#     """Return fullname users"""
#     if middlename:
#         fullname = firstname.title() + " " + lastname.title() + " " + middlename
#     else:
#         fullname = firstname + " " + lastname
#     return fullname.title()
#
#
# student = get_formatted_fullname('toshpulatov', 'ozodbek', 'izzatillayevich')
# print(student)
# student = get_formatted_fullname('toshpulatov', 'ozodbek')
# print(student)
# def build_person(firstname, lastname):
#     """Return a dictionary of information about a person."""
#     person = {'first': firstname.title(), 'last': lastname.title()}
#     return person
#
#
# student = build_person('toshpulatov', 'ozodbek')
# print(student)
# def get_formatted_name(f_name, l_name):
#     """Return a full name, neatly formatted."""
#     fullname = f_name + " " + l_name
#     return fullname
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     firstname = input("First name:")
#     if firstname == 'q':
#         break
#     lastname = input("lastname:")
#     if lastname == 'q':
#         break
#     formatted_name = get_formatted_name(firstname.title(), lastname.title())
#
#     print("\nHello " + formatted_name + "!")
# def city_country(city, country):
#     """that takes in the name
# of a city and its country"""
#     result = city.title() + "," + country.upper()
#     return result
#
#
# result_2 = city_country('tashkent', 'uzbekistan')
# print(result_2)
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         massage = "Hello" + " " + name.title() + "!"
#         print(massage)
#
#
# usernames = ['ozodbek', 'behruz', 'abduaziz']
# greet_users(usernames)

# def user_cv(ism, familiya, t_yil, t_joy,yosh=22, email='ozodbektoshpulatov04@gmail.com', phone=93_319_12_34):
#     """Foydalanuvchining malumotlari haqidagi funksiya"""
#     dict = {
#         'ism:': ism.title(),
#         'familiya:': familiya.title(),
#         'tugilgan yil:': t_yil,
#         'tugilgan joy:': t_joy.title(),
#         'email': email,
#         'phone': phone,
#         'yosh':yosh
#     }
#     return dict
#
#
# massage = user_cv('ozodbek', 'toshpulatov', 2000, 'samarqand')
# for key, value in massage.items():
#     print(key, value)


# def oraliq(min, max):
#     """range() funksiyasi"""
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#         return sonlar
#
#
# print(oraliq(1, 10))


# def max_min(son_1, son_2, son_3):
#     """3 ta sondan eng kattasini qaytaruvchi funksiya"""
#     x = max(son_1, son_2, son_3)
#     return x
#
#
# maximum = max_min(154, 145, 144)
#
# def info_doira(radius):
#     """Doiraning kattaliklarini topuvchi funksiya"""
#     dict={
#         'radius=':radius,
#         'diametr=':2*radius,
#         'uzunligi=':2*3.14*radius,
#         'yuza=':3.14*(radius**2)
#     }
#     return dict
# x=info_doira(4)
# for key,value in x.items():
#     print(key,value)

# def complex_number(number):
#     """Sonning murakkabligini aniqlaydigan funksiya!"""
#     lists=list(range(1,number))
#     numbers=[]
#     for y in lists:
#         if number%y==0:
#             numbers.append(y)
#     if number==sum(numbers):
#         return print(f"{number}-mukammal son")
#     else:
#         return print(f"{number}-murakkab son")
# complex_number(6)
#
# def tub_son(son):
#     """Tub sonni aniqlaydigan funksiya"""
#     x_list = list(range(2, son))
#     qoldiqlar = []
#     if son == 2:
#         return print(f"{son} tub son")
#     for x in x_list:
#         qoldiqlar.append(son % x)
#     if 0 in qoldiqlar:
#         return print(f"{son} murakkab son")
#     else:
#         return print(f"{son} tub son")
#
#
# tub_son(101)
# def fibonachchi(son):
#     """Fibonachhi ketma-ketlikdagi sonlarni chiqaruvchi funksiya"""
#
#     y = []
#     for x in range(son):
#         if x == 0 or x == 1:
#             y.append(x)
#         else:
#             y.append(y[x - 1] + y[x - 2])
#     return y
#
#
# print(fibonachchi(10))
# def show_employee(name,salary=9000):
#     """name and age"""
#     return print(f"name:{name} salary:{salary}")
# show_employee("Ben",12000)
# show_employee("Jessa")
# def bahola(ismlar):
#     """talabalarni baholaydigan funksiya"""
#     lugat = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism}ning bahosini kiriting:")
#         lugat[ism] = int(baho)
#         return lugat
#     talabalar = ['hasan', 'husan', 'ali', 'vali']
#     baholar = bahola(talabalar)
#     print(baholar)
