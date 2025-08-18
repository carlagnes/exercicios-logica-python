# Escreva um algoritmo que receba dois valores inteiros distintos e apresente a diferença do maior para o menor.

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("===== RESULTADO =====")
if num1>num2:
  sub = num1 - num2
  print(f"\nA diferença entre {num1} e {num2} é {sub}")
else:
  sub = num2 - num1
  print(f"\nA diferença entre {num2} e {num1} é {sub}")