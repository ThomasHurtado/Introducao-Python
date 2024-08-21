with open ('./Texto.txt') as tex:
    r = tex.readlines()
    print(r)

with open ('./Texto2.txt', 'w') as texto:
    texto.write('tenta criar ai')
