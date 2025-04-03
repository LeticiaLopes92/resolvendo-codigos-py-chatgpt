# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    print (num1 + num2)
elif operacao == "-":
   print (abs(num1 - num2))
elif operacao == "*":
    print (num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print (num1 / num2)
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Erro: Operação inválida."
print(f"O resultado da operação {num1} {operacao} {num2} é: {resultado}")