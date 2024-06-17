Nota1 = float(input("digite a primeira nota: "))
Nota2 = float(input("digite a primeira nota: "))
Nota3 = float(input("digite a primeira nota: "))
Nota4 = float(input("digite a primeira nota: "))

notas = (Nota1, Nota2, Nota3, Nota4)
soma = sum (notas)
media = (soma/len(notas))

# len mostra quantidade de valores dentro de uma lista, ela retorna o numero de elementos

print (f"A soma das notas é {soma} e a media é igual a {media}")
