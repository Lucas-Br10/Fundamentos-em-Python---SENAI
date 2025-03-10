
# Verificar se é impar ou par 

"""
Digite um numero inteiro 
Verifique se o numero é impar ou par
Escreva a mensagem correspondente 
"""


print("seja bem vindo ao sitema impar ou par")
print("Digite o numero correspondente")
numero = int(input())

resto = numero % 2 # 10 / 2 = 0

if resto != 0:  
    print("e o numero impar")
else:
    print("e o numero par")