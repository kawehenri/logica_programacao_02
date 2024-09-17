import tkinter as tk
from tkinter import simpledialog, messagebox
import tkinter.font as tkfont

#definição das 2 classes
class Produto:
    def _init_(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def get_valor_estoque(self):
        return self.quantidade * self.preco

    def _str_(self):
        return f"Produto{{nome='{self.nome}', preço={self.preco}, quantidade={self.quantidade}}}"


class SuperMarket:
    def _init_(self, root):
        self.produtos = []
        self.root = root
        self.root.title("SuperMarket")
        self.font = tkfont.Font(family="Arial", size=12)

        self.menu()

    # definição do menu pra fazer as escolhas usando while e if para quando escolher uma opção selecionar um if
    def menu(self):
        while True:
            resposta = simpledialog.askstring("Menu",
                "Escolha uma opção:\n"
                "1. Adicionar produtos\n"
                "2. Listar produtos\n"
                "3. Remover produto\n"
                "4. Calcular total em estoque\n"
                "5. Sair")
            
            if resposta is None:
                break

            opcao = int(resposta)

            if opcao == 1:
                self.adicionar_produto()
            elif opcao == 2:
                self.listar_produtos()
            elif opcao == 3:
                self.remover_produto()
            elif opcao == 4:
                self.calcular_total_estoque()
            elif opcao == 5:
                messagebox.showinfo("Saindo", "Saindo...")
                break
            else:
                messagebox.showerror("Erro", "Opção inválida")

    # função para adicionar produto
    def adicionar_produto(self):
        nome = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto")
        if nome is None:
            return
        
        quantidade = self.ler_quantidade()
        preco = self.ler_preco()

        # aqui verifica se tem o produto rodando um loop pra percorrer
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                messagebox.showwarning("Aviso", "Produto já cadastrado.")
                return

        produto = Produto(nome, quantidade, preco)
        self.produtos.append(produto)

        messagebox.showinfo("Sucesso", f"Produto {nome} adicionado com sucesso!")

    # function para ler a quantidade
    def ler_quantidade(self):
        while True:
            try:
                quantidade = int(simpledialog.askstring("Quantidade", "Digite a quantidade do produto desejada"))
                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa")
                return quantidade
            except ValueError as e:
                messagebox.showerror("Erro", f"Entrada inválida: {e}")

    #function para ler o preço
    def ler_preco(self):
        while True:
            try:
                preco = float(simpledialog.askstring("Preço", "Digite o preço do produto"))
                if preco < 0:
                    raise ValueError("O preço não pode ser negativo")
                return preco
            except ValueError as e:
                messagebox.showerror("Erro", f"Entrada inválida: {e}")

    #function para listar os produtos
    def listar_produtos(self):
        if not self.produtos:
            messagebox.showinfo("Listagem de Produtos", "Nenhum produto cadastrado.")
            return

        lista = "\n".join(str(produto) for produto in self.produtos)
        messagebox.showinfo("Lista de Produtos", lista)

    #function para remover produtos da lista 
    def remover_produto(self):
        nome = simpledialog.askstring("Remover Produto", "Digite o produto a ser removido")
        if nome is None:
            return

        produto_remover = None
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto_remover = produto
                break

        if produto_remover:
            self.produtos.remove(produto_remover)
            messagebox.showinfo("Sucesso", f"Produto {nome} removido com sucesso")
        else:
            messagebox.showerror("Erro", f"Produto {nome} não encontrado")

    #function para calcular o estoque com o calculo
    def calcular_total_estoque(self):
        total_estoque = sum(produto.get_valor_estoque() for produto in self.produtos)
        messagebox.showinfo("Total em Estoque", f"Valor total em estoque: R${total_estoque:.2f}")


if __name__== "_main_":
    root = tk.Tk()
    root.withdraw()  # aqui é pra ocultar a janela princi
    SuperMarket(root)