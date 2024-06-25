
# Criando Classe
class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:  # o denominador tem que ser diferente de zero
            return a / b
        else:
            return 'Erro: divisão por zero'

    def potenciacao(self, a, b):
        return a ** b

# Instacia da classe   -> calc = cjamar calculadora
calc = Calculadora()

# Pergunta operação

num1 = float (input ("Digite um numero: "))

op = (input("Digite a operação que deseja fazer (+), (-), (*), (/), (**): "))

num2 = float (input ("Digite mais um numero: "))

if op == "+":
    resultado = calc.soma(num1, num2)
    print(f"{num1} + {num2} = {resultado}")

elif op == "-":
    resultado = calc.subtracao(num1, num2)
    print(f"{num1} - {num2} = {resultado}")

elif op == "*":
    resultado = calc.multiplicacao(num1, num2)
    print(f"{num1} * {num2} = {resultado}")

elif op == "/":
    resultado = calc.divisao(num1, num2)
    print(f"{num1} / {num2} = {resultado}")

elif op == "**":
    resultado = calc.potenciacao(num1, num2)
    print(f"{num1} ** {num2} = {resultado}")


else: 
    print("Operação inválida. Por favor, escolha +, -, *, /, ou **.")


# Chamada da função principal


#faz uma classe com carros, dps ficar chamndo as classe