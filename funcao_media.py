# Declaração de variavel
nota1 = int(input('Primeira nota do aluno: '))
nota2 = int(input('Segunda nota do aluno: '))
nota3 = int(input('Terceira nota do aluno: '))

# Inicio da função
def media(nota1, nota2, nota3):
    valor_media = (nota1 + nota2 + nota3) /3
    return print(f'O valor da media do aluno é: {valor_media}')

# Retorno da função
media(nota1,nota2,nota3)