import os
usuarios = {}

while True:
    print()
    print(30*"=", "Menu", 30*"=")
    print("1. Cadastrar usuario.")
    print("2. Listar usuário.")
    print("3. Excluir usuário.")
    print("4. Sair.")
    print(66*"=")

    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        nome = input("Digite o nome que deseja cadastrar: ").upper()
        email = input("Digite o seu e-mail: ")
        senha = input("Digite a sua senha: ")

        usuarios[nome] = {"Nome": nome, "E-mail": email, "Senha": senha}

        print(f"usuario {nome} cadastrado com sucesso!")

    elif opcao == "2":
        if usuarios:
            print("\n--- Lista de Usuários Cadastrados---")
            for email, dados in usuarios.items():
                print(f"Nome: {dados["Nome"]}, E-mail: {dados["E-mail"]}, Senha: {dados["Senha"]}")
        else:
            print("Nenhum usuário cadastrado")

    elif opcao == "3":
        nome_remove = input("Digite o nome que deseja remover: ").upper()
        if nome_remove in usuarios:
            del usuarios[nome_remove]
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "4":
        print("Saindo do sistema!")
        break