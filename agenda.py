def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
    ==========================================
            PROJETO AGENDA EM PYTHON
    MENU:
    [1]CADASTRAR CONTATO
    [2]LISTAR CONTATO
    [3]DELETAR CONTATO
    [4]BUSCAR CONTATO PELO NOME
    [5]SAIR
    ==========================================
    ESCOLHA UMA OPÇÃO ACIMA: ''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listartContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloNome()
        else:
            sair()
        voltarMenuPrincipal = input('Deseja voltar ao menu principal? (s/n) ').lower()

def cadastrarContato():
    idContato = input('Esscolha o Id do seu contato: ')
    nome = input('Escreva o nome do seu contato: ')
    telefone = input('Escreva o telefone do seu contato: ')
    email = input('Escreva o email do seu contato: ')
    try:
        agenda = open('agenda.txt','a')
        dados = f'{idContato}; {nome}; {telefone}; {email}\n'
        agenda.write(dados)
        agenda.close
        print(f'Contato gravado com sucesso!!!')
    except:
        print('ERRO na gravação do contato')
    

def listartContato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close
    
    
def deletarContato():
    nomeDeletado = input('Digite um nome para ser deletado: ').lower()
    agenda = open('agenda.txt','r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso')
    listartContato()

def buscarContatoPeloNome():
    nome = input(f'Digite um nome a ser procurado: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Até mais...!!!')
    exit()
    


def main():
    menu()

main()

