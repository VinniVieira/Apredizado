class carros:
    def __init__(self, modelo, ano, motor, quilometragem, preço, multa): # -> parametros da minha classe "variaveis da minha classe"
        self.modelo = modelo # o self serve para acessar as Propriedade e Metodos de uma instancia 
        self.ano = ano
        self.motor = motor
        self.quilometragem = quilometragem
        self.preço = preço
        self.multa = multa

    def exibir_detalhes (self):
        detalhes = (f"Modelo: {self.modelo}\n "
                    f"Ano: {self.ano}\n "
                    f"Motor: {self.motor}\n"
                    f"Quilometragem: {self.quilometragem}\n "
                    f"Preço: {self.preço}\n "
                    f"Multas: {self.preço}\n "
                    )
        return detalhes
    
    def desc_multa (self, descricao):
        self.multa.append (descricao) #append para adicionar
    
    def verificar_multas(self):
        if self.multas:
            return True
        else:
            return False
        

