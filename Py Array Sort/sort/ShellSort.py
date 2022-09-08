# Classe repsonsável pela implementação do Shell Sort
#

# Py Array Sort / sort / Shellsort
# @author MRX
# Version : 1.0.0

class Shellsort:

    def sort(self, array):

        tamanho = len(array) // 2

        while tamanho > 0:
            for i in range(tamanho):
                self.gapInsertionSort(array, i, tamanho)

            tamanho = tamanho // 2

        return array

    def gapInsertionSort(self, array, inicio, gap):

        for i in range(inicio + gap, len(array), gap):
            valorAtual = array[i]
            posicao = i

            while posicao >= gap and array[posicao - gap] > valorAtual:
                array[posicao] = array[posicao - gap]
                posicao -= gap

            array[posicao] = valorAtual
