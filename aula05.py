lista = ['gomes', 10, True, 1.60]

lista1 = [1,2,3,4,5,6,7,8,9,10]

# indices negativos sao tratados de maneira especial, o -1 é considerado o ultimo elemento

lista_int = [10,5,3,49,8,3,4,9,42,15,16,13,11,20]
print(lista_int)
lista_int.sort()

print(lista_int)
lista_int.sort(reverse=True)

print(lista_int)
print(f'Lista ordenada direto no print: {sorted(lista_int)}')

# remove, pop, del

nomes = ('Gomes', 'Oliveira', 'Joao' , 'Pedro' , 'Dias')
'''

print(nomes)
nomes.remove('Dias')
print(nomes)
print.pop(3)
print(nomes)

'''

'''
# remove mais de um elemento da lisa
del nomes[2:4]
print(nomes)

'''

lista_nomes = []

novo_nome = input('Digite um novo nome: ')
lista_nomes.append(novo_nome)

print(lista_nome)