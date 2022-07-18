def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro: informe um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar os dados! \033[m')
            return 0 
        else:
            return numero

def linha(tamanho = 42):
    return '-' * tamanho

def cabeçalho(txt):
    print(linha)
    print(txt.center(42))
    print(linha)

def menu(lista):
    print('Menu Principal ')
    c = 1
    for itens in lista:
        print(f'\033[33m{c}\033[m - \033[34m{itens}\033[m')
        c += 1
    print(linha)
    opc = leiaInt('\033[32mO que o Sr(a) gostaria? \033[m')
    return opc