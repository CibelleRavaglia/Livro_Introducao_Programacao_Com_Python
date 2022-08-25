"""
Escreva um programa que leia dois números.
Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão.
Utiliza apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender o quociente da divisão de dois números como a
quantidade de vezes que podemos retirar o dividor do dividendo.
Logo 20 dividido por 4 = 5, uma vez que podemos substrai 4 cinco vezes de 20.

"""
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")