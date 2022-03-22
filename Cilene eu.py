desejado = int(input('Número de variável desajado: '))
total = int(input('Numero total:'))
porcentagem = (desejado / total) * 100
print('{:.2f}%'.format(porcentagem))


# Cilene mais completo
eu = int(input('Digite o numero da variável eu: '))
tu = int(input('Digite o numero da variável tu: '))
ele = int(input('Digite o numero da variável ele: '))
nos = int(input('Digite o numero da variável nós: '))
vos = int(input('Digite o numero da variável vós: '))
eles = int(input('Digite o numero da variável eles: '))
total = eu + tu + ele + nos + vos + eles
print('Eu {:.2f}%'.format((eu / total) * 100))
print('Tu {:.2f}%'.format((tu / total) * 100))
print('Ele {:.2f}%'.format((ele / total) * 100))
print('Nós {:.2f}%'.format((nos / total) * 100))
print('Vós {:.2f}%'.format((vos / total) * 100))
print('Eles {:.2f} %'.format((eles / total) * 100))
