# mydict={
#     'Float':'o\'nlik son',
#     'For':'biror amalni qayta-qayta bajarish sikli',
#     'integer':'butun son',
#     'if':'shartlarni tekshirish operatori',
#     'Boolean':'Mantiqiy qiymat'
# }
# for x,y in sorted(mydict.items()):
#     print(f"{x}-{y}")
country_capital={
    'uSA':'Washington',
    'russia':'Moscow',
    'uzbekistan':'Tashkent',
    'kazakhstan':'Astana',
    'italy':'Rome',
    'malaysia':"Kuala-Lampur"
}

print("Countries")
for key in sorted(country_capital.keys()):
    print(f"{key.upper()}") 
print("Capitals")
for value in sorted(country_capital.values()):
    print(value)
txt=input("Istalgan davlatni kiriting:")

capital=country_capital.get(txt.lower())
#x=txt.upper()
# for y in key:
#  if txt.upper() in y:
#     print(country_capital[txt])
