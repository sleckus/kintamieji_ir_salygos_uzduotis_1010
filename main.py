import random

# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus). Parašykite kodą,
# kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".

# name = input('iveskite savo varda: ')
# lastName = input('iveskite savo pavarde: ')
# birthYear = input('iveskite savo gimimo metus: ')
# currentYear = input('iveskite dabartinius kalendorinius metus: ')
#
# print(f'As esu',name,lastName,f'man yra',int(currentYear)-int(birthYear), f'metai(u)')

# 2. Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.

# number1 = random.randint(0,4)
# number2 = random.randint(0,4)
#
# if number1>=number2:
#     print(round(int(number1) / int(number2), 2))
# else:
#     print(round(int(number2) / int(number1), 2))

# Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

# number1 = random.randint(0,25)
# number2 = random.randint(0,25)
# number3 = random.randint(0,25)

# nepabaigta

# 4 Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite ​random.randint(x,x)​ funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.

# a = random.randint(1,10)
# b = random.randint(1,10)
# c = random.randint(1,10)

# visada gausis trikampis???? whats the point tikrinti?

# 5 Sukurkite keturis kintamuosius ir ​random.randint(x,x)​ funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

# a = random.randint(0,2)
# b = random.randint(0,2)
# c = random.randint(0,2)
# d = random.randint(0,2)
#
# nuliai = [a, b, c, d].count(0)
# vienetai = [a, b, c, d].count(1)
# dvejetai = [a, b, c, d].count(2)
#
# print(f'nuliu skaicius',nuliai,f'vienetai ', vienetai, f'dvejetai ', dvejetai)

# 6  Naudokite funkcija random.randint(x,x).
# Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10. Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose [],
# 0 -  (), didesni už 0 {}.   [-4],  (0)
#
# a = random.randint(-10,10)
# b = random.randint(-10,10)
# c = random.randint(-10,10)
#
# if a<0:
#     print(f'[',int(a),f']')
# elif a==0:
#     print(f'(', int(a), f')')
# else:
#     print(f'{{', int(a), f'}}')
#
# if b<0:
#     print(f'[',int(b),f']')
# elif b==0:
#     print(f'(', int(b), f')')
# else:
#     print(f'{{', int(b), f'}}')
#
# if c<0:
#     print(f'[',int(c),f']')
# elif c==0:
#     print(f'(', int(c), f')')
# else:
#     print(f'{{', int(c), f'}}')

# 7 Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida.
# Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama.
# Žvakių kiekį generuokite ​random.randint(x,x)​ funkcija nuo 5 iki 3000.

# candlePrice = 1
# candleSum = random.randint(5,3000)
#
# if candleSum < 1000:
#     print(int(candleSum) * int(candlePrice), f' kaina be nuolaidos')
#     print(f'zvakiu skaicius', int(candleSum))
# elif  candleSum >= 1000:
#     print(int(candleSum)*int(candlePrice)*0.97, f' kaina su 3proc nuolaida.')
#     print(f'zvakiu skaicius', int(candleSum))
# elif candleSum >= 2000:
#     print(int(candleSum) * int(candlePrice) * 0.96, f' kaina su 4proc nuolaida.')
#     print(f'zvakiu skaicius',int(candleSum))

# 8 Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100. Paskaičiuokite jų aritmetinį vidurkį.
# Ir aritmetinį vidurkį atmetus tas reikšmes,
# kurios yra mažesnės nei 10 arba didesnės nei 90. Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)

average = round((a+b+c)/3)
print(f'aritmetinis vidurkis: ',average)



