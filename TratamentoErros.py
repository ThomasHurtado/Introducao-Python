try:
    n = int(input('Digite um numero: '))
except:
    print('Erro ao digitar o numero')
else:
    print(f'Numero digitado: {n}')

while True:
    try:
        n = int(input('Digite um numero: '))
    except ValueError:
        print('Erro ao digitar o numero')
    except KeyboardInterrupt:
        print('teste')
        break