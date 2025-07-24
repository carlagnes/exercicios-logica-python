# Faça um algoritmo que leia uma temperatura do teclado em Fahrenheit e apresente-a convertida em graus Celsius. 

fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
celsius = ((fahrenheit - 32) * 5) / 9

print(f"{fahrenheit} Farenheit equivale a {celsius} graus Celsius.")
