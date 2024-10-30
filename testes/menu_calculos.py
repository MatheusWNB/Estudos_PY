import cmath


print('Olá, seja muito bem vindo ao Menu de cálculos. Para iniciar digite o seu nome, por favor:')
nome_usuario = input('Digite o seu nome: ')

print()

print(f'Certo {nome_usuario}, para começarmos eu preciso que você selecione oque gostaria de calcular: ')
print()

def menu_opcoes_calculos():
    print('(Média escolar) = 1')
    print('(Conversor de temperatura) = 2')
    print('(Fórmula de Bhaskara) = 3')
    print('(Adição, subtração, multiplicação ou divisão) = 4')
    print('(Sair do aplicativo) = 5')

def resposta_do_usuario(resposta_usuario_menu):
    match resposta_usuario_menu:

        case '1':
            print('Para calcular a sua média eu preciso que você me informe as suas notas:')
            
            n1 = float(input('Nota 1: '))
            n2 = float(input('Nota 2: '))
            n3 = float(input('Nota 3: '))
            n4 = float(input('Nota 4: '))

            calculo_media_notas = (n1 + n2 + n3 + n4) / 4

            print(f'{nome_usuario}, a sua média é {calculo_media_notas:.2f}.')

            if calculo_media_notas >= 7:
                print('Parabéns, você foi aprovado!')

            else:
                print('Sinto muito, você foi reprovado.')

        case '2':
            print('Certo, qual unidade de medida gostaria de converter?')
            print('(Fahrenheit para Celsius) = 1')
            print('(Celsius para Fahrenheit) = 2')
            
            resposta_case_2 = input('Digite sua escolha: ')

            if resposta_case_2 == '1':
                print('Certo, qual a temperatura em °F?: ')
                temperatura_fahrenheit = float(input('Temperatura: '))

                fahrenheit_celsius = (temperatura_fahrenheit - 32) // 1.8
                    
                print(f'O resultado é {fahrenheit_celsius} °C.')

            elif resposta_case_2 == '2':
                print('Certo, qual a temperatura em Celsius?: ')
                temperatura_celsius = float(input('Temperatura: '))

                celsius_fahrenheit = temperatura_celsius * 1.8 + 32

                if celsius_fahrenheit > 32:
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F. A temperatura está acima do ponto de congelamento.')

                elif celsius_fahrenheit == 32:
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F. A temperatura está no ponto de congelamento.')

                else: 
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F. A temperatura está abaixo do ponto de congelamento.')

        case '3':
            print(f'Certo {nome_usuario}, para calcularmos eu preciso que me informe os valores da equação: ')
            
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))

            calculo_discriminante = (b ** 2) - 4 * a * c

            calculo_bhaskara_x1 = (-b + cmath.sqrt(calculo_discriminante)) / (2 * a)
            calculo_bhaskara_x2 = (-b - cmath.sqrt(calculo_discriminante)) / (2 * a)

            print('As raízes da equação são: ')            
            print(f"x' = Real -> {calculo_bhaskara_x1.real:.2f} e imaginária -> {calculo_bhaskara_x1.imag:.2f}.")
            print(f'x" = Real -> {calculo_bhaskara_x2.real:.2f} e imaginária -> {calculo_bhaskara_x2.imag:.2f}.')

        case '5':
            return False

    return True

continuar = True
while continuar:
    menu_opcoes_calculos()
    resposta_usuario_menu = input('Digite sua escolha: ')
    print()
    continuar = resposta_do_usuario(resposta_usuario_menu)
    if resposta_usuario_menu == '5':
        print('Encerrando aplicativo...')
    elif resposta_usuario_menu <='4':
        print('Aperte "Enter" para voltar ao menu.')

    else:
        print('Nenhuma alternativa foi selecionada, por favor digite novamente.')
    print()

    
    

    




    
 







