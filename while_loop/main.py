# cars = ["lacetti", "nexia", "toyota", "nexia", "malibu", "nexia"]
# while 'nexia' in cars:  # toki nexia cars ruyhatida ekan
#     cars.remove('nexia')
# print(cars)
# talabalar = ["hasan", "husan", "olim", "shavkat"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting:")
#     print(f"{talaba.title()} baholadi")
#     baholangan_talabalar[talaba] = baho
# for talaba, baho in baholangan_talabalar.items():
#     print(f"{talaba.title()}ning bahosi {baho} ga teng!")
# savol = "Qanday mahsulot buyurtma berasiz:"
# mahsulotlar = []
# qiymat = True
# while qiymat:
#     buyurtma = input(savol)
#     mahsulotlar.append(buyurtma)
#     javob = input("Yana mahsulot buyurtma berasizmi?(ha/yoq):")
#     if javob == 'yoq':
#         qiymat = False
# for mahsulot in mahsulotlar:
#     print(f"sizning buyurtmangiz:{mahsulot}")

print("e-bozor mahsulotlari va ularning nanarxlari")
mahsulotlar = ['non', 'pomidor', 'guruch', 'sabsi', 'piyoz', 'gusht', 'ziravor']
mahsulot_narx = {}
while True:
    mahsulot = input("Mahsulotni kiriting:")
    narx = input(f"{mahsulot.title()}ning narxini kiriting:")
    mahsulot_narx[mahsulot] = narx
    savol = input("Yana mahsulot va narxini kiritasizmi?(ha/yoq):")
    if savol == 'yoq':
        break
product = input("product kiriting:")
for mahsulot, narx in mahsulot_narx.items():
    if product == mahsulot:
        print(f"{mahsulot.title()}ning narxi {narx} so'mga teng")
