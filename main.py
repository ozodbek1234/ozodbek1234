
"""
car_1={
    'model':'lacetti',
    'color':'white',
    'price':15000,
    'karoka':'avtomat'
}
car_2={
    'model': 'cobalt',
    'color': 'black',
    'price': 14000,
    'karoka': 'mexaika'
}
car_3= {'model':'nexia 3',
    'color':'red',
    'price':10000,
    'karoka':'avtomat'}
cars=[car_1,car_2,car_3]
for car in cars:
    print(f"{car['model'].title()}",
          f"{car['color']}",
          f"{car['price']}$",
          f"{car['karoka']}"
          )
print(car_1)
print(car_2['model '])

malibus = []
for n in range(10):
        new_car = {
        'model': 'malibu',
        'color': None,
        'year': 2020,
        'km': 0,
        'price': None,
        'karobka': 'avtomat'
    }
malibus.append(new_car)
for malibu in malibus[:3]:
    malibu['color']='black'
for malibu in malibus[6:]:
    malibu['color']='white'
    malibu['karobka']='mexanika'
for malibu in malibus:
    if malibu['karobka']=='avtomat':
        malibu['price']=40000
for malibu in malibus:
    print(malibu.values())

dasturchilar={
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
}
for ism,dasturlash_tillari in dasturchilar.items():
    print(f"\n{ism.title():}: ",end='')
    for til in dasturlash_tillari:
        print(f"{til.upper()} ",end='')
"""
#lug'at ichida lug'at
# hamkasblar={
#     'ali':{'familiya':'valiyev',
#            't_yil':2000,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#
#     }

# }
# for ism, dict_2 in hamkasblar.items():
#     print(f"{ism.title()} {dict_2['familiya'].title()}. \n"
#     f"Ma'lumoti:{dict_2['malumot']}. \n"
#     f"tug\'ilgan yili:{dict_2['t_yil']}. \n"
#     "Quyidagi dasturlash tillarini biladi:"
#     )
#     for til in dict_2['tillar']:
#         print(til.upper())

olim_1={
    'name':'Ilon Musk',
    't_yil':1971,
    'boyligi':200,
    'kompaniyalari':['Tesla', 'SpaceX', 'Neuralink', 'The Boring Company', 'Zip2', 'X.com', 'OpenAI', 'Musk Foundation']
}
olim_2={
    'name':'Bill Gates',
    't_yil':1955,
    'boyligi':100,
    'kompaniyalari':['Microsoft','Microsoft Store','Xbox Game Studios']
}
olim_3={
    'name':'Mark Zuckerberg',
    't_yil':1984,
    'boyligi':33,
    'kompaniyalari':['A Terrible Fate Records','Facebook']
}
men=[olim_1,olim_2,olim_3]
for man in men:
    print(f"\n{man['name']}.\n"
          f"{man['t_yil']}-yilda tug'ilgan.\n"
          f"boyliigi:${man['boyligi']} mlrd.\n"
          # f"Kompaniyalari:{man['kompaniyalari']}"
          "Kompaniyalari:"
          )

    for kompaniya in man['kompaniyalari']:
        print(kompaniya)

