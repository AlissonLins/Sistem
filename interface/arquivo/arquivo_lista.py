from interface import cabeçalho
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        True

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        cabeçalho('{PESSOAS CADASTRADAS')
        for linha in a:
          dado = linha.split(';') 
          dado[1]= dado[1].replace('\n','')
          print(f'{dado[0]<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um erro na hora de escrever os dadaos.')
        else:
            print(f'O usuário {nome} foi cadastrado com sucesso.')
            a.close()