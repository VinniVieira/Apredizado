while True:
    num = int(input("digite um numero que queira saber a sua taboada até o 10: "))

    for i in range (1,10):
        resultado = num * i
        print (f"{num} + {i} = {resultado}")

    terminar = input ("Deseja continuar? S ou N? ")

    if terminar == "N":
        break