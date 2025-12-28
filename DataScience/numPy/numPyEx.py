import numpy as np
import sys

a = [1, 2, 3, 4, 5]
b = np.array([1,2,3,4,5])

print(a)
print(b)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

#Array 1D (x)
d1 = np.array([1,2,3])
print(d1)
print(d1.shape) #formato do array
print(d1.ndim) #quantas dimensões
print(d1.dtype) # tipo de dados

#Array 2D (x, y)
d2 = np.array([[1,2,3], [1,2,3]])
print(d2)
print(d2.shape) #formato do array
print(d2.ndim) #quantas dimensões
print(d2.dtype) # tipo de dados

#Array 3D (x, y, z)
d3 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(d3)
print(d3.shape) #formato do array
print(d3.ndim) #quantas dimensões
print(d3.dtype) # tipo de dados

#soma Array

n1 = np.array([1,2,3])
n2 = np.array([1,2,3])

resultado = np.add(n1, n2)
print(resultado)

#selecionar itens em Arrays

c = np.array([[2,3,4,5], [6,7,8,9]])
print(c)

#array[row, colu] encontrar o 8
c[1,2]

#regressivo encontrar o 8
c[1,-2]

#encontrar linha 0 e todas as colunas
c[0, :]

#mostrar somente a coluna 1 3 e 7
a[:, 1] 
