lista = [1,2,34,67,21,11,16,43,55,10,21,43,56,87]
print(lista[0])
print(lista[0:5])

lista.sort(reverse=True)
print(f'Lista ordena {lista}')

lista.remove(11)#o remove vc tem q passar o valor que vc quer remover da lista, caso tenha dois iguais ele só remove 1
#o pop e o del remove por indice
lista.pop(0)
#o del sera usado o indice do elemento que vc quer eliminar, podendo ser mais de um como 0:5
del lista[0:2]

#função append, adiciona outro valor a sua lista
nome = 'gomes'
lista.append(nome)
print(lista)

#função insert, adiciona outra a sua lista em x posição
lista.insert(2, 'jonas')

#como substituir
lista[2] = 'kleber'

#in
print('belo' in lista)

#um dos usos do not é com o in
print('belo' not in lista)


#if else finalmente
if 'kleber' in lista:
    #esse bloco só sera executado se a condição for verdadeira
    print('sim o kleber esta na lista')
else: #esse bloco so sera executado se a condição for falsa
    print('não o kleber não esta na lista')

notas = []
print(30*'-', 'BOLETIM ESCOLAR' ,30*'-')
numero_usuario1 = int(input('Digite um numero: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite um numero: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite um numero: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite um numero: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite um numero: '))
notas.append(numero_usuario5)

# Len conta a quantidade de elementos dentro da lista
quantidade_notas = len(notas)

# sum ira somar todos os elementos da lista
soma = sum(notas)

media = soma / quantidade_notas

print(f'As notas são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A media é: {media}')

'''
    #TODO: Situação
    Aprovado >= 7
    Recuperção >= 5 
    Reprovado
'''
if media >= 7:
    print(f'Aprovado com media {media}')

elif media >= 5:
    print(f'Recuperação com media {media}')

else:
    print(f'Reprovado com media {media} ')






