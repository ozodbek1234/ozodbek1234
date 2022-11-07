# while darslari
# savol = "Istalgan sonni kiriting"
# savol += "(to'xtatish uchun 'exit' deb yozing):"
# qiymat=''
# while qiymat !='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)
#     else:
#         print("Dastur tugadi!")
# savol = "Istalgan sonni kiriting"
# savol += "(to'xtatish uchun 'exit' deb yozing):"
# qiymat = True
# while qiymat:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         qiymat = False
#         print("Dastur tugadi!")
#     else:
#         print(float(qiymat) ** 2)
# savol = "Istalgan sonni kiriting"
# savol += "(to'xtatish uchun 'exit' deb yozing):"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         print("Dastur tugadi")
#         break
#     else:
#         print(float(qiymat) ** 2)
son = 0
# while son < 10:
#     son += 1
#     if son % 2 == 0:
#         continue
#     else:
#         print(son, end=' ')

# savol = "Yaxshi ko'rgan kitobingizni kiriting"
# savol += "(to'xtatish uchun 'stop' deb yozing):"
# kitoblar=[]
# while True:
#     qiymat = input(savol)
#     kitoblar.append(qiymat.capitalize())
#     if qiymat == 'stop':
#         break
#     else:
#         print(kitoblar)
# savol = "Yoshingizni kiriting"
# savol += "(Dasturni to'xtatish uchun 'exit' yoki 'quit deb yozing):"
#
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         print("Dastur tugadi!")
#         break
#
#     if int(yosh) <= 7:
#         narx = 2000
#         print(f"Kirish chiptasi {narx} so'm!")
#         break
#     if int(yosh) > 7 and int(yosh) <= 18:
#         narx = 3000
#         print(f"Kirish chiptasi {narx} so'm!")
#         break
#     if int(yosh) > 18 and int(yosh) <= 65:
#         narx = 10_000
#         print(f"Kirish chiptasi {narx} so'm!")
#         break
#     if int(yosh) > 65:
#
#         print("Kirish chiptasi tekin")
#         break
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
while True:
    qiymat = (input(savol))

    if qiymat.capitalize() == 'Exit':
        print("Dastur tugadi!")
        break
    elif int(qiymat) < 0:
        print("Musbat son kiriting!")
        break
    else:
        ildiz =(float(qiymat) ** (1 / 2))
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
# ismlar=[]
# print("Yaqin do'stlaringiz ro'yhatini tuzamiz.")
# n=1
# while True:
#     savol=f"{n}-do'stingizni ismini kiriting:"
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasizmi? (ha/yoq)")
#     if javob=='ha':
#         n+=1
#         continue
#     else:
#         break
# print("ro'yhat tuzildi")
# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())
#
# print("Do'stlaringiz yoshini aniqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = ("Do'stingizni ismini kiriting:")
#     yosh = input(f"{ism} yoshini kiriting:")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ism qo'shasizmi? (ha/yoq):")
#     if javob == 'yoq':
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism} {yosh} yoshda")
