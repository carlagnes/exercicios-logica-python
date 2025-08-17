# Escreva um algoritmo que receba três valores inteiros distintos e indique qual deles é o maior, e qual deles é o menor.

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1>num2 and num1>num3:
  num_maior = num1

elif num2>num1 and num2>num3:
  num_maior = num2

else:
  num_maior = num3

if num1<num2 and num1<num3:
  num_menor = num1

elif num2<num1 and num2<num3:
  num_menor = num2

else:
  num_menor = num3

print("\n========= RESULTADO =========")
print(f"Entre os números {num1}, {num2} e {num3}, o MAIOR é {num_maior} e o MENOR é {num_menor}.")