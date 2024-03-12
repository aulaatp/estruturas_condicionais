#entradas de dados para os valores
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
#entradas condicionais
#caso 1 - mostrar o quadrado da soma
if n1 > n2:
    soma = n1 + n2
    print(f"O quadrado da soma dos números é {soma**2}")
#caso 2 - mostrar a soma dos quadrados
elif n2 > n1:
    resultado = n1**2 + n2**2
    print(f"A soma dos quadrados é {resultado}")
else:
    print("Os números são iguais!")