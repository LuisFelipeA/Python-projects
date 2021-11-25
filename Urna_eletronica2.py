#O Brasil tem um grave problema quando falamos em política, porém podemos ter ações que podem melhorar alguns dos fatores. A primeira que teremos é criar um algoritmo base para a Urna Eletrônica. Nesse algoritmo teremos apenas 5 canditados por enquanto:
#1 - Vincent Vega
#2 - Rick Dalton
#3 - Shoshanna Dreyfus
#4 - Beatrixx Kido
#5 - Jules Winnfield
#Vocês devem criar um algoritmo que pergunte quantos eleitores irão participar, cada eleitos terá direito a apenas um voto, porém se realizar um voto errado (um número de candidato que não existe), tem 5 chances até informar um voto válido. No final deve informar a porcentagem de votos de todos os candidatos e quem foi eleito. Não precisa considerar segundo turno. Caso ocorra um empate, mostrar quais os nomes empatados e porcentagem de empate.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
candidato5 = 0

eleitor = 0
voto_valido = 0
tentativas = 5

while eleitor < 10:
    
    voto = int(input("Escolha um candidato de 1 a 5: "))

    while voto > 5 and tentativas > 0:
        voto = int(input("Escolha um candidato de 1 a 5: "))
        tentativas -= 1

    if voto == 1:
        candidato1 = candidato1 + 1
        eleitor = eleitor + 1
        voto_valido += 1
    elif voto == 2:
        candidato2 = candidato2 + 1
        eleitor = eleitor + 1
        voto_valido += 1
    elif voto == 3:
        candidato3 = candidato3 + 1
        eleitor = eleitor + 1
        voto_valido += 1
    elif voto == 4:
        candidato4 = candidato4 + 1
        eleitor = eleitor + 1
        voto_valido += 1
    elif voto == 5:
        candidato5 = candidato5 + 1
        eleitor = eleitor + 1
        voto_valido += 1
    else:
        print("Voto invalido")
        eleitor = eleitor + 1


    print(f"eleitor: {eleitor}")


print("-"*15)
candidato1 = candidato1*100/voto_valido

candidato2 = candidato2*100/voto_valido

candidato3 = candidato3*100/voto_valido

candidato4 = candidato4*100/voto_valido

candidato5 = candidato5*100/voto_valido

if candidato1 > candidato2 and candidato1 > candidato3 and candidato1 > candidato4 and candidato1 > candidato5:
    vencedor = "Candidato 1 = Vincent Vega"

elif candidato2 > candidato1 and candidato2 > candidato3 and candidato2 > candidato4 and candidato2 > candidato5:
     vencedor = "Candidato 2 = Rick Dalton"

elif candidato3 > candidato1 and candidato3 > candidato2 and candidato3 > candidato4 and candidato3 > candidato5:
     vencedor = "Candidato 3 = Shoshanna Dreyfus"

elif candidato4 > candidato1 and candidato4 > candidato2 and candidato4 > candidato3 and candidato4 > candidato5:
     vencedor = "Candidato 4 = Beatrixx Kido"

elif candidato5 > candidato1 and candidato5 > candidato2 and candidato5 > candidato3 and candidato5 > candidato4:
    vencedor = "Candidato 5 = Jules Winnfield"

else:
    vencedor = "Nenhum dos candidatos foi eleito"

    

print("Candidato eleito:")
print(vencedor)
print("-"*15)

print("Porcentagem de votos:")
print(f"Candidato 1: {candidato1:.2f}%")
print(f"Candidato 2: {candidato2:.2f}%")
print(f"Candidato 3: {candidato3:.2f}%")
print(f"Candidato 4: {candidato4:.2f}%")
print(f"Candidato 5: {candidato5:.2f}%")

if candidato1 == candidato2 and candidato1 > 20:
    print("Empate entre candidato 1 e candidato 2")
elif candidato1 == candidato3 and candidato1 > 20:
    print("Empate entre candidato 1 e candidato 3")
elif candidato1 == candidato4 and candidato1 > 20:
    print("Empate entre candidato 1 e candidato 4")
elif candidato1 == candidato5 and candidato1 > 20:
    print("Empate entre candidato 1 e candidato 5")
elif candidato2 == candidato3 and candidato2 > 20:
    print("Empate entre candidato 2 e candidato 3")
elif candidato2 == candidato4 and candidato2 > 20:
    print("Empate entre candidato 2 e candidato 4")
elif candidato2 == candidato5 and candidato2 > 20:
    print("Empate entre candidato 2 e candidato 5")
elif candidato3 == candidato4 and candidato3 > 20:
    print("Empate entre candidato 3 e candidato 4")
elif candidato3 == candidato5 and candidato3 > 20:
    print("Empate entre candidato 3 e candidato 5")
elif candidato4 == candidato5 and candidato4 > 20:
    print("Empate entre candidato 4 e candidato 5")
elif candidato1 == candidato2 == candidato3 == candidato4 == candidato5:
    print("A votação tera que ser feita novamente")
else:
    print("Não houve empate")   