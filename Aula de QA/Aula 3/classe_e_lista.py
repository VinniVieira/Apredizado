

linguagens_tupla = ('java', 'python', 'C+', 'java Script')
linguagens_lista = list(linguagens_tupla)

print (f"A variavel é: {type(linguagens_tupla)}")
print (f"E se tranformou em: {type(linguagens_lista)}")


linguagens_lista.append("Malbolge") # permite adicionar um argumento
print (linguagens_lista)

linguagens_lista.extend(["Malbolge", "ruby"]) # permite adicionar mais de um argumento
print (linguagens_lista)

linguagens_lista.pop(o) # remove o
print (linguagens_lista)