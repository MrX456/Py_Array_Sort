# Classe repsonsável pela implementação do Bubble Sort
#

# Py Array Sort / sort / Bubblesort
# @author MRX
# Version : 1.0.0

class Bubblesort:

    def sort(self, array):

        tamanho = len(array) - 1
        ordenado = False

        while not ordenado:
            ordenado = True

            for i in range(tamanho):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    ordenado = False

        return array


