nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a primeira nota: "))
nota3 = float(input("digite a primeira nota: "))
nota4 = float(input("digite a primeira nota: "))

notas = (nota1, nota2, nota3, nota4)
media = (sum (notas)/len(notas))

# len mostra quantidade de valores dentro de uma lista, ela retorna o numero de elementos

print (f"As notas são: {notas} e a media é igual a {media}")
 