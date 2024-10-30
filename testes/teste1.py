def tela_inicial():
    nome = input('Digite o seu nome:')
    print(f'Olá {nome}, seja muito bem-vindo! Oque gostaria de calcular?')

def mostrar_menu():
    print('(Cálculo de média) = 1')
    print('(Cálculo conversor de temperatura) = 2')
    print('(Menu) = 3')
    print('(Sair do programa) = 4')

def resposta_usuario(resp):
    match resp:
        case '1':
            print('Olá')
            print('Digite "3" para voltar ao menu.')
            resp1 = input()
            if resp1 == '3':
                return continuar
            else:
                print('Processo finalizado.')
                return False

        case '2':
            print('Bem vindo')
            print('Digite "3" para voltar ao menu.')
            resp2 = input()
            if resp2 == '3':
                return continuar
            else:
                print('Processo finalizado.')
                return False

        case '3':
            mostrar_menu()

        case '4':
            print('Saindo do programa...')
            return False

        case _:
            print('Opção inválida. Tente novamente.')

    return True

tela_inicial()

continuar = True
while continuar:
    mostrar_menu()
    resp = input()
    continuar = resposta_usuario(resp)













