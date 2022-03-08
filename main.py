#calculadora
from time import sleep

linhas = '-#.' * 20

#Limpar_tela
def limpar():
    print("\n" * 130)

#voltar_menu
def menu():
    sleep(1)
    print(linhas)
    voltarM = int(input('''
                   deseja voltar pro menu inicial? 
                         [1] Sim       [2] não
                                
=> '''))

    if voltarM == 1:
        limpar()
        calculadora()

    else:
        limpar()
        quit()


def calculadora():

    print(linhas)
    while True:

        # Escolhas
        print('''
                            [MENU 1]
                          [1] Soma
                          [2] Subtração 
                          [3] Multiplicação
                          [4] Divisão 
                          [5] Mais opçoes 
                          [6] Sair
                                                      
                     ''')

        # Linhas
        print(linhas)

        # Escolha
        escolha = int(input('Digite sua escolha:  '))

        print(linhas)

        # Funções
        if escolha == 1:
            num_1 = int(input('Digite o primeiro numero: '))
            num_2 = int(input('Digite o segundo numero: '))
            print('A soma de {} e {} é {}'.format(num_1, num_2, (num_1 + num_2)))
            menu()

        elif escolha == 2:
            num_1 = int(input('Digite o primeiro numero: '))
            num_2 = int(input('Digite o segundo numero: '))
            print('A Subtração de {} e {} é {}'.format(num_1, num_2, (num_1 - num_2)))
            menu()

        elif escolha == 3:
            num_1 = int(input('Digite o primeiro numero: '))
            num_2 = int(input('Digite o segundo numero: '))
            print('A multiplicação de {} e {} é {}'.format(num_1, num_2, (num_1 * num_2)))
            menu()

        elif escolha == 4:
            num_1 = int(input('Digite o primeiro numero: '))
            num_2 = int(input('Digite o segundo numero: '))
            print('A Divisão de {} e {} é {:.2f} e seu resto é {}'.format(num_1, num_2, (num_1 / num_2), (num_1 % num_2)))
            menu()

        # Mais_opções
        if escolha == 5:
            print('''                   
                            [MENU 2]
                                        
                          [1] Expoente
                          [2] Fatorial 
                          [3] Raiz quadrada
                          [4] Voltar 
                          [5] Sair
                                      
                                 ''')
            escolha_pag2 = int(input('Digite a opção desejada: '))

            if escolha_pag2 == 1:
                num_3 = int(input('\nDigite a base: '))
                num_4 = int(input('\nDigite o expoente: '))
                print(pow(num_3, num_4))
                menu()

            if escolha_pag2 == 2:
                n = int(input("Digite o valor de n: "))
                fat = 1
                i = 2
                while i <= n:
                    fat = fat * i
                    i = i + 1
                print("O valor de %d! eh =" %n, fat)
                menu()

            if escolha_pag2 == 3:
                n = int(input("Digite o valor de n: "))
                print('a raiz quadrada de {} é {}' .format(n, pow(n, 2)))

            if escolha_pag2 == 4:
                menu()
            if escolha_pag2 == 4:
                quit()

        elif escolha == 6:
            quit()

        elif escolha != True:
            erro = int(input('''
            Escolha invalida, deseja tentar novamente? 
                        [1] Sim       [2] não
                        
=> '''))
            if erro == 1:
                limpar()
                calculadora()
            else:
                    limpar()
                    quit()
                    sleep(1)


calculadora()
