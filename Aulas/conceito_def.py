

def carro_matheus():
    print("pegeut 206 turbo")

    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()
    carro_matheus()


def menu():
        print("Menu da calculadora")
        print("1 - Soma")
        print("2 - Subtrai")
        print("3 - sair")

def somar(n1, n2):
        return n1 + n2

def subtrai(n1, n2):
        return n1 - n2

def verificacaoopcao(opcao):
    if opcao == 1:
        na1 = float(input("Digite o numero 1"))
        na2 = float(input("Digite o numero 2"))
        print(somar(na1, na2))
        
    elif opcao == 2:
        na1 = float(input("Digite o numero 1"))
        na2 = float(input("Digite o numero 2"))
        print(subtrai(na1, na2))

def calculadora():
        while True:
            menu()
            opcao = int(input("escolha uma opção"))
            verificacaoopcao(opcao)
