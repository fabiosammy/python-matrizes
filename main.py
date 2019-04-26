#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import random
import time
import logging
import threading
import Queue

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

def multiplica_linha_coluna(queue, queue_resultados, matrizA, matrizB):
    while True:
        i, j = queue.get()
        valor = 0
        for k in range(len(matrizB)):
            valor = valor + matrizA[i][k] * matrizB[k][j]
        queue.task_done()
        queue_resultados.put((i, j, valor))

if __name__ == '__main__':
    linhas, colunas = 400, 400

    print("{}: Gerando matrizes".format(time.strftime('%c')))
    matrizA = cria_matriz(linhas, colunas)
    matrizB = cria_matriz(linhas, colunas)
    matrizC = numpy.zeros(shape=(linhas,colunas))

    print("{}: Multiplicando matrizes".format(time.strftime('%c')))
    queue = Queue.Queue()
    queue_resultados = Queue.Queue()
    for i in range(2):
        worker = threading.Thread(target=multiplica_linha_coluna, args=(queue, queue_resultados, matrizA, matrizB,))
        worker.setDaemon(True)
        worker.start()

    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            queue.put((i, j))

    while not queue_resultados.empty():
        i, j, valor = queue_resultados.get()
        matrizC[i][j] = valor
        queue_resultados.task_done()

    print("{}: Resultado:{}".format(time.strftime('%c'), matrizC))
