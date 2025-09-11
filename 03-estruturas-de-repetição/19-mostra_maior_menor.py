# Utilizando estruturas de repetição, faça um algoritmo que receba 10 números 
# inteiros e apresente o maior e o menor valores lidos.

print("Digite 10 números inteiros.")


for i in range(4):
    while True:
        num = int(input("Digite um número: "))
        break


    if num<0:
        num_menor = num
    else:
        num_maior = num
 
print("---Resultado---")
print("O maior número é:", num_maior)
print("O menor número é:", num_menor)