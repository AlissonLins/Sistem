from interface import util
from interface import lib,arquivo_lista,arquivoExiste,criararquivo,lerArquivo,cadastrar
from time import sleep

arq = 'Listagem.txt'
if not arquivoExiste(arq):
   criararquivo(arq)

while True:
    resposta = util.menu('Listar Usuários', 'Cadastrar Usuários','Finalizar Sistema' )
    if resposta == 1:
        # Opção de criar um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de Cadastrar um novo usuário
        util.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = util.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de finalizar o sistema
        util.cabeçalho('Finalizando o sistema...')
        break
    else:
        print('\033[31mErro! Opção inválida.\033[m')
        sleep(2)