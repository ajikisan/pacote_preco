# Módulo para realizar a validação dos dados de entrada digitadas.
# strip tira os espaços antes e depois

def leia_valor_moeda(mensagem):
    msg_valido = False
    while not msg_valido:
        valor_moeda = str(input(mensagem)).replace(",", ".").strip()
        if valor_moeda.isalpha() or valor_moeda == "":
            print(
                f"\033[0;31mAtenção!: \"{valor_moeda}\" Valor Inválido!\033[m")
            break
        else:
            msg_valido = True
        return float(valor_moeda)


def leia_valor_inteiro(mensagem):
    while True:
        try:
            valor_moeda = int(input(mensagem))
        except (ValueError, TypeError):
            print(
                "\033[31mErro: Por gentileza, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mNão houve digitação de números.\033[m")
            return 0
        else:
            return valor_moeda


def leia_valor_float(mensagem):
    while True:
        try:
            valor_moeda = float(input(mensagem))
        except (ValueError, TypeError):
            print(
                "\033[31mErro: Por gentileza, digite um número real válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mAção interrompida.\033[m")
            return 0
        else:
            return valor_moeda
