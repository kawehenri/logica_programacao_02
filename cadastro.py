lista_usuario = []
import os

while True:
    print()
    print(30*"=", "Menu", 30*"=")
    print("1. Cadastrar usuario.")
    print("2. Listar usuário.")
    print("3. Excluir usuário.")
    print("4. Buscar pelo usuario")
    print("5. Inserir em uma posição")
    print("6. Sair.")
    print(30*"=", "Menu", 30*"=")

    opcao = input("Digite a opção desejada: ")

#Cadastrar usuario
    if opcao == "1":
        nome = input("Digite o nome que deseja cadastrar: ").upper()

        if nome != "":
            lista_usuario.append(nome)
            print(f"Usuário {nome} cadastrado com sucesso!")
        else:
            print("Digite algum valor!")

#Listar usuario
    elif opcao == "2":
        for i, n in enumerate(lista_usuario):
            print(f"{i + 1}º {n}")

#Excluir usuario
    elif opcao == "3":

        posicao = int(input("Digite o numero de usuario que deseja excluir: "))

        for j, _ in enumerate(lista_usuario):
            if j == posicao:
                lista_usuario.pop(j)
                print(f'O usuario da posição {j} foi removido. ')


        '''
        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print("Usuário removido com sucesso.")
        '''

#Buscar pelo nome
    elif opcao == '4':
        nome_buscar = input('Digite o nome que deseja encontrar na lista').upper()

        if nome_buscar != '':
            for i in lista_usuario:
                if i == nome_buscar:
                    print(i)

#Inserir em uma posição
    elif opcao == '5':
        novo_nome = input('Digite o nome que deseja inserir: ')
        posicao_nome = int(input('Digite a posição do nome que deseja inserir: '))

        #Correção da posição
        posicao_nome -= 1
        if posicao_nome >= 0 and posicao_nome <= len(lista_usuario):
            lista_usuario.insert(posicao_nome, novo_nome)

        else:
            print('Posição invalida. ')           

#Sair do codigo
    elif opcao == '6':
        print('Saindo do sistema! ')
        break

    else:
        print('Digite uma opção valida. ')
        
    