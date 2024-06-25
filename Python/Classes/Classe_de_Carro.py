# Crie um classe de carros no python, com marca, modelo, ano, cor, motor, quilometragem preço

class carros:
    def __init__(self, modelo, ano, motor, quilometragem, preço): # -> parametros da minha classe "variaveis da minha classe"
        self.modelo = modelo # o self serve para acessar as Propriedade e Metodos de uma instancia 
        self.ano = ano
        self.motor = motor
        self.quilometragem = quilometragem
        self.preço = preço

    def exibir_detalhes (self):
        detalhes = (f"Modelo: {self.modelo}\n "
                    f"Ano: {self.ano}\n "
                    f"Motor: {self.motor}\n"
                    f"Quilometragem: {self.quilometragem}\n "
                    f"Preço: {self.preço}\n "
                    )
        return detalhes
    


meu_carro = carros ("Ford Mustang", 1969, "V8", 1000, 100000)
print (meu_carro.exibir_detalhes())