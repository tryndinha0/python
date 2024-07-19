numeros = [1,2,3,4,6,7,8,9,10]
nomes = ['Daniel','Duda','Lucas','Claudia']
lista = [2005,2024]
#num = int(input('Digite um número e mostraremos a tabuada: '))
soma = 0
try:
    for valor in numeros:
        soma += valor
        print({soma})
    media = soma/len(numeros)
    print(f'A média dos valores é {media}')
except ZeroDivisionError:
    print('Não há valores na lista')
except Exception:
    print('Erro')