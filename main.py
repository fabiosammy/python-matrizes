#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import random

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

def multiplica_linha_coluna(matrizA, matrizB, i, j):
    valor = 0
    for k in range(len(matrizB)):
        valor = valor + matrizA[i][k] * matrizB[k][j]
    return valor

if __name__ == '__main__':
    linhas, colunas = 400, 400

    matrizA = cria_matriz(linhas, colunas)
    matrizB = cria_matriz(linhas, colunas)
    matrizC = numpy.zeros(shape=(linhas,colunas))

    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            matrizC[i][j] = multiplica_linha_coluna(matrizA, matrizB, i, j)

    print("Resultado:{}".format(matrizC))
