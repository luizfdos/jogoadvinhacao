from random import randint
from time import sleep
from termcolor import colored

def jogo():
    title = "ADIVINHAÇÃO"
    print(colored(19 * '-=-', 'yellow'))
    print(colored(f'{title:^60}', 'blue'))
    print(colored(19 * '-=-', 'yellow'))
    print(colored('Vou pensar em um número entre 0 e 5. Tente advinhar...', 'blue'))
    print(colored(19 * '-=-', 'yellow'))
    numero = randint(0,5)
    numerostr = str(numero)
    escolha = str(input(("Em qual número estou pensando? ")))
    print(colored('PROCESSANDO...', 'magenta'))
    sleep(1)
    if escolha == numerostr:
        print(colored(f"PARABÉNS! Você VENCEU! Eu estava pensando no numero {numero}!", 'green'))
        jogarnovamente()
    elif escolha != numerostr:
      print(colored(f"VOCÊ PERDEU! Eu pensei no número {numero} e não em {escolha}!", 'red'))
      jogarnovamente()

def jogarnovamente():
        escolha = str(input('Deseja jogar novamente?(S/N) '))
        if escolha.upper() == 'S':
            jogo()
        elif escolha.upper() == 'N':
            print(colored('Até a proxima!!', 'blue'))
            sleep(3)
            exit(0)
        else:
            print(colored('Opção inválida!!','red'))
            jogarnovamente()

jogo()