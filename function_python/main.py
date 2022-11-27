# def ism_yosh(ism, yosh):
#     """Foydalauvchi tug'ilga yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2022 - yosh}-yilda tug'ilgan")
#
#
# ism_yosh("ozodbek", 22)

# def kvadrat_kub(son):
#     """Sonning kvadrat va kubini hisoblaydigan funksiya!"""
#     print(f"{son**2}\n{son**3}")
# kvadrat_kub(2)
# print(kvadrat_kub.__doc__)
# def juft_toq(son):
#     """Sonning juft yoki toqligini hisoblaydigan funksiya!"""
#     if son % 2 == 0:
#         print(f"{son} juft son!")
#     elif son % 2 != 0:
#         print(f"{son} toq son!")
#     else:
#         print("Nol yoki manfiy son!")
#
#
# juft_toq(7)
# print(juft_toq.__doc__)
# def min_max(son_1, son_2):
#     """2 ta sonning kattasini topuvchi dastur!"""
#     if son_1 > son_2:
#         print(f"{son_1} {son_2} dan katta")
#     elif son_1 == son_2:
#         print("Sonlar teng!")
#     else:
#         print(f"{son_1} soni {son_2} sonidan kichik")
#
#
# min_max(5, 6)
# def sonning_darajasi(son, daraja=2):
#     """Sonning darajasini hisoblaydigan funksiya"""
#     print(f"{son} sonining {daraja}-darajasi = {son ** (daraja)}")
#
#
# print(sonning_darajasi.__doc__)
# sonning_darajasi(4)
# def qoldiqni_tekshir(son):
#     """Sonning 2 dan 10 gacha bo'lgan sonlardan qaysilariga qoldiqsiz bo'linishini topuvchi dastur"""
#     for x in range(2, 11):
#         if son % x == 0:
#             print(x, end=' ')
#
#
# qoldiqni_tekshir(20)
