
# Numeros Pares em um Intervalo 

"""
solicite dois numeros inteiros ao usuario 
Representando o inicio e o fim de um intervalo
Mostre todos os numeros pares nesse intervalo (incluindo limite inicial e final, se forem pares)
"""

n1 = int(input("digite o numero 1"))
n2 = int(input("digite o numero 2"))

for y in range(n1, n2): 
    if y % 2 == 0:
        print("o numero e par: ", y)

