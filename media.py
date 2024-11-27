nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota:"))
nota3 = float(input("Escreva a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3
print('a media é:', media)
if media < 6 :
    print('Reprovado')
else:
    print('Aprovado')
