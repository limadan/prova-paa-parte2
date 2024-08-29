import time
import numpy as np

class SortMethods:
    def __init__(self):
        pass

    def insertion_sort(self, array):
        comparisons = 0
        movements = 0
        
        start_time = time.time()  # Início do cronômetro
        n = len(array)
        for i in range(1, n):
            aux = array[i]
            movements += 1
            j = i - 1
            
            while j >= 0 and aux < array[j]:
                comparisons += 1
                array[j + 1] = array[j]
                movements += 1
                j -= 1
            
            if j >= 0:  # Conta a comparação que falha
                comparisons += 1
            
            array[j + 1] = aux
            movements += 1

        # Medir o tempo de execução
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return comparisons, movements, elapsed_time

    def select_sort(self, array):
        comparisons = 0
        movements = 0

        start_time = time.time()  # Início do cronômetro
        n = len(array)
        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                comparisons += 1
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]
            movements += 3  # troca de dois elementos

        # Medir o tempo de execução
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return comparisons, movements, elapsed_time

    def shell_sort(self, array):
        comparisons = 0
        movements = 0

        start_time = time.time()  # Início do cronômetro
        n = len(array)
        h = 1
        while h < n:
            h = h * 3 + 1

        while h > 1:
            h //= 3
            for i in range(h, n):
                aux = array[i]
                movements += 1
                j = i

                while j >= h and array[j - h] > aux:
                    comparisons += 1
                    array[j] = array[j - h]
                    movements += 1
                    j -= h

                if j >= h:  # Conta a comparação que falha
                    comparisons += 1

                array[j] = aux
                movements += 1

        # Medir o tempo de execução
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return comparisons, movements, elapsed_time

    def heap_sort(self, v):
        total_comparisons = 0
        total_movements = 0
        tamanho_vetor = len(v)

        start_time = time.time()  # Início do cronômetro

        for i in range(tamanho_vetor // 2 - 1, -1, -1):
            comparisons, movements = self.constroi_heap(v, tamanho_vetor, i)
            total_comparisons += comparisons
            total_movements += movements

        for i in range(tamanho_vetor - 1, 0, -1):
            v[0], v[i] = v[i], v[0]
            total_movements += 3
            comparisons, movements = self.constroi_heap(v, i, 0)
            total_comparisons += comparisons
            total_movements += movements
        
        # Medir o tempo de execução
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return total_comparisons, total_movements, elapsed_time

    def constroi_heap(self, v, n, i):
        comparisons = 0
        movements = 0
        pai = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2
        comparisons += 3

        if esquerda < n and v[esquerda] > v[pai]:
            pai = esquerda
            comparisons += 2

        if direita < n and v[direita] > v[pai]:
            pai = direita
            comparisons += 2

        if pai != i:
            v[pai], v[i] = v[i], v[pai]
            movements += 3
            sub_comparisons, sub_movements = self.constroi_heap(v, n, pai)
            comparisons += sub_comparisons
            movements += sub_movements
        
        return comparisons, movements

    def merge_sort(self, v):
        start_time = time.time()  # Início do cronômetro

        comparisons, movements = self._merge_sort(v)

        # Medir o tempo de execução
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        return comparisons, movements, elapsed_time

    def _merge_sort(self, v):
        comparisons = 0
        movements = 0
        if len(v) > 1:
            meio = len(v) // 2 
            esquerda = v[:meio]
            direita = v[meio:]
            left_comp, left_mov = self._merge_sort(esquerda)
            right_comp, right_mov = self._merge_sort(direita)
            comparisons += left_comp + right_comp + 3
            movements += left_mov + right_mov

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                comparisons += 1
                if esquerda[i] < direita[j]:
                    v[k] = esquerda[i]
                    i += 1
                else:
                    v[k] = direita[j]
                    j += 1
                k += 1
                movements += 1

            while i < len(esquerda):
                v[k] = esquerda[i]
                i += 1
                k += 1
                movements += 1

            while j < len(direita):
                v[k] = direita[j]
                j += 1
                k += 1
                movements += 1

        return comparisons, movements

def generate_descending_vector(size):
    return list(range(size, 0, -1))

def test_algorithms():
    sizes = [100, 1000, 10000, 1000000]
    sorter = SortMethods()

    results = []

    for size in sizes:
        vector = generate_descending_vector(size)

        for sort_name, sort_method in {
            "Insertion Sort": sorter.insertion_sort,
            "Selection Sort": sorter.select_sort,
            "Shell Sort": sorter.shell_sort,
            "Heap Sort": sorter.heap_sort,
            "Merge Sort": sorter.merge_sort
        }.items():
            vector_copy = vector.copy()
            comparisons, movements, elapsed_time = sort_method(vector_copy)
            results.append({
                'algorithm': sort_name,
                'size': size,
                'comparisons': comparisons,
                'movements': movements,
                'time': elapsed_time
            })

    # Criar uma tabela usando numpy
    dtype = [('Algorithm', 'U20'), ('Size', 'i4'), ('Comparisons', 'i8'), ('Movements', 'i8'), ('Time (s)', 'f8')]
    np_results = np.array([(
        result['algorithm'],
        result['size'],
        result['comparisons'],
        result['movements'],
        result['time']
    ) for result in results], dtype=dtype)

    # Imprimir a tabela
    print("\nTabela de Resultados:")
    print(np_results)

if __name__ == "__main__":
    test_algorithms()
