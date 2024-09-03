lista = []

nome1 = input('digite um nome: ')
lista.append(nome1)
nome2 = input('digite um novo nome: ')
lista.append(nome2)

lista.sort()
print(lista)

if nome1 and nome2 in lista:
    print(f'sim o {nome1} e o {nome2} esta na lista')
else:
    print(f'não o {nome1} e o {nome2} não esta na lista')

numero_sorte = 7

numero_usuario = int(input('digite um numero: '))
if numero_usuario == numero_sorte:
    print('parabens voce ganhou!')
else:
    print('que pena voce errou, tente novamente')