"""
!1-mashq
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())
!2-mashq
login=input("Loginingizni kiriting:")
if login=="admin":
    print(f"Xush kelibsiz,{login.title()}.Foydalanuvchilar ro'yhatini ko'rasizmi?")
elif login != "admin":
    print(f"Xush kelibsiz,{login.title()}!")   
!3-mashq
son_1=int(input("1-sonni kiriting:"))
son_2=int(input("2-sonni kiriting:"))
if son_1==son_2:
    print("Sonlar teng ekan!")
else:
    print("Sonlar teng emas!")
!Bir necha shartlarni tekshirish 
*2-mashq
yosh=int(input("Yoshingizni kiriting:"))
if yosh<4 or yosh>60:
    print("Bepul")
if yosh<18:
    print("Chipta narxi 1000 so'm!")
elif yosh>18 and yosh<60:
    print("Chipta narxi 2000 so'm!")
!4-mashq
mahsulotlar=['pomidor', 'sabsi','guruch','go"sht','bodring','piyoz','yog"','non','Coca-Cola','choy']
savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni kiriting:"))
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("savat bo'sh")
!7-mashq
son=int(input("Butun son kiriting:"))
for x in range(2,11):
   # print(x)
    if son%x==0:
        print(x)

foydalanuvchilar=[]
for n in range(5):
    txt=input("Login kiriting:")
    foydalanuvchilar.append(txt)
yangi_login=input("Yangi login kiriting:")
if foydalanuvchilar:
    for foydalanuvchi in foydalanuvchilar:
        if yangi_login==foydalanuvchi:
            print("Login band, yangi login tanlang")
            
else:
    print("Xush kelibsiz, foydalanuvchi!")
"""
mydict={
    'Ozodbek':'Resmi note 9',
    'Muslimbek':'Galaxy A32',
    'Ibrohim':'Iphone X',
    'Jahongir':'Galaxy A32'
}
# key=mydict.keys()
# value=mydict.values()
# print(set(value))
# print(mydict.items())
# print(mydict["Ozodbek"])
# for x in key:
#     print(x)
# for y in value:
#     print(y)
# for x,y in mydict.items():
#     print(f"key:{x}")
#     print(f"value:{y}")
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m")