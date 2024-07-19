#exercicio 1 
pessoa = {'nome':'Daniel', 'idade':18, 'cidade':'RJ'}
#exercicio 2
pessoa['idade'] = 20
print(pessoa['idade'])
pessoa['profissao'] = 'desenvolvedor'
print(pessoa['profissao'])
del pessoa['cidade']
#exercicio 3
def numeros_quadrados():
    for numero in range(1,5):
        print(numero**2)
        
    
numeros_quadrados()

#exercicio 4 
if 'nome' in pessoa:
    print('A chave "pessoa" existe')
else:
    print('A chave "pessoa" não existe')

#exercicio 5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)