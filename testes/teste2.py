def tela_inicial():
    nome = input('Digite o seu nome: ')
    print(f'Olá {nome}, seja muito bem-vindo! O que gostaria de calcular?')

def mostrar_menu():
    print('(Cálculo de média) = 1')
    print('(Conversor de temperatura) = 2')
    print('(Sair) = 3')

def resposta_usuario(resp):
    match resp:
        case '1':
            print('Opção 1: Cálculo de média (a implementar)')

        case '2':
            print('Opção 2: Conversor de temperatura (a implementar)')

        case '3':
            print('Saindo do programa...')
            return False

        case _:
            print('Opção inválida. Tente novamente.')

    return True

# Executando o programa
tela_inicial()

continuar = True
while continuar:
    mostrar_menu()
    resp = input('Digite sua escolha: ')
    continuar = resposta_usuario(resp)
