# Classe = Obejeto -> 

class Teste:
    def __init__(self, modelo, ano, cor, quilometragem) :
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def exibir_detalhes (self):
        detalhes = (f"Modelo: {self.modelo}\n "
                    f"Ano: {self.ano}\n "
                    f"cor: {self.cor}\n "
                    f"Quilometragem: {self.quilometragem}\n "

                )
        return detalhes    
    

# criar um VAR para o carro
seu_carro = input ("Digite o seu carro na seguinte ordem: modelo, ano, cor, quilometragem: ")

# Separar as string em substring ".split"
modelo, ano, cor, quilometragem = seu_carro.split(",")

#tranfosmando as str de ano e km em int
ano = int(ano)
quilometragem = int(quilometragem)

# Criar uma instância da classe Teste
carro_objeto = Teste(modelo, ano, cor, quilometragem)

# Exibindo os detalhes do carro chando a função de detlhes
print (carro_objeto.exibir_detalhes())