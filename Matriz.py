import numpy as np

matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(matriz)

#Sempre começa pelo indice 0

print(matriz[0])
print(matriz[0][0])
soma = 0

for i in range(matriz.shape[0]): #shape[0] = linhas
    for j in range(matriz.shape[1]): #shape[1] = colunas 
        soma = soma + matriz[i][j]

print(soma)
