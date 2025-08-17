# Considere as seguintes propriedades sobre os triângulos:
# O comprimento de cada lado em um triângulo é menor que a soma dos outros dois lados;
# Triângulos equiláteros têm os comprimentos dos 3 lados iguais;
# Triângulos isósceles: têm os comprimentos de dois lados iguais;
# Triângulos escalenos: têm os comprimentos dos três lados diferentes;
# Faça um algoritmo que receba três valores X, Y e Z, e verifique se eles podem ser os comprimentos dos lados de um triângulo. Se forem, verificar se o triângulo é equilátero, isósceles ou escaleno. Informe, também, caso não formem um triângulo.

x = float(input("Digite o valor do primeiro lado: "))
y = float(input("Digite o valor do segundo lado: "))
z = float(input("Digite o valor do terceiro lado: "))


if x+y>z or x+z>y or y+x>z or y+z>x:
  triangulo = True


  if triangulo == True and (x==y) and (y==z):
    print("O seu triângulo é equilátero.")
  elif triangulo == True and (x==y) and (y!=z) or (x==z) and (x!=y):
    print("O seu triângulo é isósceles.")
  else:
    print("O seu triângulo é escaleno.")  
else:
    print("Os valores informados não formam um triângulo.")
