# Faça um algoritmo em que o usuário informe seu nome e sua idade. Apresente uma mensagem como:
# “Olá, Carla! Você nasceu no ano de 1997.”
# OBS: Para o cálculo do ano, desconsidere o dia e mês de nascimento.

nome = str(input("\nDigite o seu nome: "))
idade = int(input("Digite sua idade: "))

ano_nascimento = (2025-idade) - 1

print(f"Olá, Carla! Você nasceu no ano de {ano_nascimento}.")



