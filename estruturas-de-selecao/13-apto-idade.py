# A confederação brasileira de natação promoverá eliminatórias para o próximo mundial. Fazer um algoritmo que receba a idade de um nadador e determine (imprima) a sua categoria segundo a tabela a seguir:

print("\n===== NÍVEL PARA COMPETIÇÃO =====")
idade = int(input("Digite sua idade: "))


if idade<=3:
  print("Inapto a competir.")
elif idade>=4 and idade<=8:
  print("Sua categoria é Infantil A.")
elif idade>=8 and idade<=10:
  print("Sua categoria é Infantil B.")
elif idade>=11 and idade<=13:
  print("Sua categoria é Juvenil A.")
elif idade>=14 and idade<=17:
  print("Sua categoria é Juvenil B.")
elif idade<=3:
  print("Inapto a competir.")
else:
  print("Sua categoria é Sênior.")