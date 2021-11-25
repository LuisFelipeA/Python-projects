# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda sim(s) ou não(n)")

participacao_crime = []
inocente = []

a = input("Telefonou para a vítima?")

if a == "s":
    participacao_crime.append(a)
else:
    inocente.append(a)

b = input("Esteve no local do crime?")

if b == "s":
    participacao_crime.append(b)
else:
    inocente.append(b)

c = input("Mora perto da vítima?")

if c == "s":
    participacao_crime.append(c)
else:
    inocente.append(c)

d = input("Devia para a vítima?")

if d == "s":
    participacao_crime.append(d)
else:
    inocente.append(d)

e = input("Já trabalhou com a vítima?")

if e == "s":
    participacao_crime.append(e)
else:
    inocente.append(e)

if len(participacao_crime) == 5:
    print("Assassino")
elif len(participacao_crime) == 3 or len(participacao_crime) == 4:
    print("Cumplice")
elif len(participacao_crime) == 2:
    print("Suspeito")
else:
    print("Inocente")