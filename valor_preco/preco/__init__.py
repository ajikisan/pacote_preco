# Autora: Mirian Ajiki Molicawa
# Criação do módulo Preço com as funções:
# aumentar, diminuir, dobrar e mostrar o valor metade do preço da compra
# formatacao_valor : inserção do "R$"" e 2 casas decimais separadas por vírgula
# resumo  impressão dos valores resumidos na tela
# Parâmetro Preço: O preço que será calculado
# Parâmetro Taxa:  o percentual aumentado ou reduzido sobre o valor informado
# Parâmetro Formato: quando informado verdadeiro separa em duas casas decimais
# Return: resultado dos cálculos formatados


def aumentar(preco=0, taxa=0, formato=False):
    resultado = preco + (preco * taxa/100)
    return resultado if formato is False else formatacao_valor(resultado)


def diminuir(preco=0, taxa=0, formato=False):
    resultado = preco - (preco * taxa/100)
    return resultado if formato is False else formatacao_valor(resultado)


def dobro(preco=0, formato=False):
    resultado = preco * 2
  #  return resultado if not formato else preco(resultado)
    return resultado if formato is False else formatacao_valor(resultado)


def metade(preco=0, formato=False):
    resultado = preco / 2
    return resultado if formato is False else formatacao_valor(resultado)


# def formatacao_valor(preco=0, simbolo='R$'):
 #   return f'{simbolo}{preco:>.2f}'.replace(".", ",")

def formatacao_valor(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace(".", ",")


def resumo(preco=0, taxaa=10, taxar=5):
    print("-"*50)
    print("Resumo do Valor".center(50))
    print("-"*50)
    print(f'Valor do Preço Analisado: \t{preco}')
    print(f'Metade do Preço \t\t{metade(preco,True)}')
    print(f'Dobro de Preco \t\t\t{dobro(preco,True)}')
    print(f'{taxaa}% de aumento \t\t\t{aumentar(preco,taxaa,True)}')
    print(f'{taxar}% de redução \t\t\t{diminuir(preco,taxar,True)}')
    print("-"*50)
