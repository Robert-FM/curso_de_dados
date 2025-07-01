def Titulo(txt):
    print('*'*30)
    print(txt.center(30))
    print('*'*30)

def Menu():
    print(f'1 - Soma')
    print(f'2 - Subtração')
    print(f'3 - Multiplicação')
    print(f'4 - Divisão')
    print(f'5 - Sair')
    print('*'*30)

def Operações(operação):
    if operação == 1:
        return num1 + num2
    elif operação == 2:
        return num1 - num2
    elif operação == 3:
        return num1 * num2
    elif operação == 4:
        return num1 / num2

def printar():
    print()
    print('-'*30)
    print(f'O resultado é {Operações(escolha)}.')
    print('-'*30)
    print()
    
def escolher():
    return int(input('Escolha sua opção [1/2/3/4/5]: '))
    


#################################################################################
import time

escolha = 0

while True:
    Titulo("Calculadora's Kepler")
    Menu() 
    escolha = escolher()
    print('-'*30)
    time.sleep(0.5)
    print()
    
    if escolha == 5:
        break

    if escolha in range(1,5):
        num1 = int(input('Digite o primeiro número: '))
        time.sleep(0.5)
        print()
        num2 = int(input('Digite o segundo número: '))
        time.sleep(0.5)
        printar()
    else:
        print('Opção inválida. Tente novamente.')

time.sleep(0.5)
print(f'Fim do programa')