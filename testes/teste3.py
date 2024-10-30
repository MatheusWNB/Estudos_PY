nomes = []

def menu_inicial():
    print('Por favor, coloque o seu nome e um nome de um conhecido ou familiar(mínimo 1)')
    print()
    nome = input('Digite o seu nome (obrigatório):')
    nome1 = input('Digite o nome de um conhecido ou familiar:')
    nomes.append(nome1)
    nomes.append(nome)
    print()

def opcoes_escolha():    
    print('Gostaria de adicionar mais pessoas ou seguir para a próxima etapa?')
    print('Adicionar mais pessoas = 1')
    print('Prosseguir para a próxima etapa = 2')
    print('Fechar aplicativo = 3')
    print('Visualizar pessoas adicionadas = 4')
    print()

def add_pessoas():
    if len(nomes)>= 4:
        print('Não é possível adicionar mais pessoas')
        print()
        voltar_menu = input('Pressione "ENTER" para voltar ao menu.')
        print()
        
    elif len(nomes) == 3:
        print('Digite o nome da pessoa que deseja adicionar:')
        nome3 = input('')
        nomes.append(nome3)
        print('Pessoa adicionada com sucesso!')
        print()    
                
    elif len(nomes) == 2:
        print('Digite o nome da pessoa que deseja adicionar:')
        nome2 = input('')
        nomes.append(nome2)    
        print('Pessoa adicionada com sucesso!')
        print()
        
def resposta_usuario(resp1):
    match resp1:

        case '1':
            add_pessoas()

        case '2':
            print('Digite o seu cpf por favor:')

        case '3':
            print('Encerrando aplicativo...')
            return False
        
        case '4':
            print(nomes)
            voltar_menu = input('Pressione "ENTER" para voltar ao menu.')
        
        case _:
            print('Opção inválida. Digite novamente a sua escolha:')
    
    return True

menu_inicial()

continuar = True
while continuar:
    opcoes_escolha()
    resp1 = input('Digite a sua escolha:')
    continuar = resposta_usuario(resp1)
    voltar_menu = input('Pressione "ENTER" para voltar ao menu.')
   



    


    
    


    
















