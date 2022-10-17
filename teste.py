from valor_preco import preco
from valor_preco import dado

# Programa Principal - Leitura de valores

# import preco
# from preco import dobro, diminuir  # Traz as funções especificadas daí não precisa colocar o módulo.
# print(f'A metade de R${valor_moeda} é R${metade(valor_moeda)}')
# import dado  # Módulo criado para validar os valores digitado pelo usuário.
# valor_moeda = float(input("Digite o preço: R$ "))


# Leitura de valores utilizando o módulo dado.py para validar as entradas de valores digitados
valor_moeda = dado.leia_valor_moeda("Digite o preço da moeda.: R$ ")
# valor_moeda = dado.leia_valor_inteiro("Digite o valor inteiro do preço.: R$ ")
# valor_moeda = dado.leia_valor_float("Digite o preço separado por ponto.: R$ ")

# Método que vai pegar o valor digitado e calcular a taxa de aumento 10% e redução 5%
preco.resumo(valor_moeda)
# Método Resumo traz taxa de aumento (taxaa) 20% e taxa de redução (taxar) 7%
preco.resumo(valor_moeda, 20, 7)
# Método Resumo traz a taxa de aumento (taxaa) 80% e taxa de redução (taxar) 20%
preco.resumo(valor_moeda, 80, 20)
