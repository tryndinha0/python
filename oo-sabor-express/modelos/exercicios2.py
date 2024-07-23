#1
class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro('Fusca','Azul',1970)
#2
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria, ativo, capacidade,avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.avaliacao = avaliacao
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
    def listar_restaurante ():
       for restaurante in Restaurante.restaurantes:
           print(f'{restaurante.nome} | {restaurante.categoria} | {"Ativo" if restaurante.ativo==True else "Inativo"} | {restaurante.capacidade} | {restaurante.avaliacao}')
        


restaurante_exemplo = Restaurante('Rio Sul','Goumert',True,200,10)

Restaurante.listar_restaurante()

#3 feito no 2
#4
print(restaurante_exemplo)
#5
class Cliente:
    def __init__(self,email,senha,idade,cpf):
        self.email = email
        self.senha = senha
        self.idade = idade
        self.cpf = cpf

cliente1 = Cliente('a@','b342Sc',18,13324434)
cliente1 = Cliente('d@','e+4Fmlz.',30,25644563)
cliente1 = Cliente('g@','h¨fxz@1',19,65635354)

