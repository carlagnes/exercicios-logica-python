# Faça um algoritmo que leia uma temperatura do teclado em graus Celsius e apresente-a convertida em graus Fahrenheit.

celsius = float(input("\nDigite a temperatura em Celsius: "))
fahrenheit = ((celsius * 9) / 5) + 32

print(f"{celsius} graus Celsius equivale a {fahrenheit} Fahrenheit.")