
print("Digite valor de A")
valorA = float(input())

print("Digite valor de B")
valorB = float(input())

print("Digite valor de C")
valorC  = float(input())

delta = valorB ** 2 - 4 * valorA  * valorC

x1 = (- valorB + delta ** (0.5)) / (2 * valorA)

x2 = (- valorB - delta ** (0.5)) / (2 * valorA)

print("Valor da Raiz", x1)

print("Valor da Raiz", x2)