# try-except
# yosh=input("Yoshingizni kiriting:")
# try:
#     yosh=int(yosh)
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadingiz!")
# print("Dastur tugadi!")

# try-except-else

# yosh = input("yoshingizni kiriting:")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz!")
# else:
#     print(f"Siz {2022 - yosh} yilda tug'ilgansiz!")

# valueError

# yosh = input("yoshingizni kiriting:")
# try:
#      yosh = int(yosh)
# except ValueError:
#      print("Butun son kiritmadingiz!")
# else:
#     print(f"Siz {2022 - yosh} yilda tug'ilgansiz!")

# ZeroDivisionError
# x, y = 10, 5
# try:
#     y/(x - 5)
# except ZeroDivisionError:
#     print("Nolga bo'lib bo'lmaydi!")
# mevalar=['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yhatda {len(mevalar)} ta meva bor holos")

#keyError
user={
    'username':'admin',
    'gmail':'ozodbektoshpulatov04@gmail.com',
    'phone':"933191234"
}
key="tel"
try:
    print(f"Foydalanuvchi:{user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas!")