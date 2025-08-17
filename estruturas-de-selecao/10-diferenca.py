# Escreva um algoritmo que receba três valores inteiros distintos e apresente a diferença entre o maior e o menor.

print("\n===== DIFERENÇA ENTRE 3 VALORES =====")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1>num2 and num1>num3:
  maior = num1
 
elif num2>num1 and num2>num3:
  maior = num2

else:
  maior = num3

if num1<num2 and num1<num3:
  menor = num1
 
elif num2<num1 and num2<num3:
  menor = num3

else:
  menor = num3

sub = maior - menor

print("\n====== RESULTADO ======")
print(f"MAIOR: {maior}")
print(f"MENOR: {menor}")
print(f"DIFERENÇA: {sub}")
