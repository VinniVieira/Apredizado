num1 = float(input("Digite um numero: "))
op = str(input("Digite uma operação: "))
num2 = float(input("Digite um numero: "))

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("Você digitou algum caracter errado")