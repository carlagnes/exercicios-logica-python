# Uma escola faz o pagamento de seus professores por hora/aula. Faça um algoritmo que calcule e exiba o salário mensal pago a um professor. Sabe-se que o há três níveis de professores, com valores de hora/aula conforme segue:
# Professor nível 1: R$ 20,00 por hora/aula Professor nível 2: R$ 25,00 por hora/aula Professor nível 3: R$ 30,00 por hora/aula

nivel = int(input("Digite seu nível: "))
aulas_ministradas = int(input("Digite o número de aulas ministradas: "))

if nivel == 1:
  salario_mensal = aulas_ministradas * 20  
elif nivel == 2:
  salario_mensal = aulas_ministradas * 25 
else:
  salario_mensal = aulas_ministradas * 30 

print(f"Seu salário mensal é de {salario_mensal}")