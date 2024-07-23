class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
#1
restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'
#2
restaurante_praca.nome = 'Praça'
print(restaurante_praca.nome)
#3
print(f'A instância restaurante_praca está: ' "Ativo" if restaurante_praca.categoria==True else "Inativo")
#4
categoria = Restaurante.categoria
#5
restaurante_praca.nome = 'Bristô'
#6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast-Food'
#7
print(f'A categoria da instância restaurante_pizza é {restaurante_pizza.categoria}')
#8
restaurante_pizza.categoria = 'Ativo'
#9
print(f'O nome da instância restaurante_pizza é {restaurante_pizza.nome}')
print(f'A categoria do restaurante_pizza é {restaurante_pizza.categoria}')
#música
class Musica:
    musicas = []

    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    def listar_musica():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('Under Pressure', 'Queen & David Bowie',248)
musica2 = Musica('The Trooper','Iron Maiden', 245)
musica3 = Musica('Hotel California', 'Eagles',390)

Musica.listar_musica()
        