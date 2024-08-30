import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import time

class SortMethods:
    def __init__(self):
        pass

    def insertion_sort(self, array):
        print("Início do Insertion Sort")
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

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Fim do Insertion Sort")
        return comparisons, movements, elapsed_time

    def select_sort(self, array):
        print("Início do Selection Sort")
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

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Fim do Selection Sort")
        return comparisons, movements, elapsed_time

    def shell_sort(self, array):
        print("Início do Shell Sort")
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

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Fim do Shell Sort")
        return comparisons, movements, elapsed_time

    def heap_sort(self, v):
        print("Início do Heap Sort")
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
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Fim do Heap Sort")
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
        print("Início do Merge Sort")
        start_time = time.time()  # Início do cronômetro

        comparisons, movements = self._merge_sort(v)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Fim do Merge Sort")
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

def generate_vector(size, vector_type):
    if vector_type == "OrdC":
        return list(range(size))
    elif vector_type == "OrdD":
        return list(range(size, 0, -1))
    elif vector_type == "OrdA":
        return random.sample(range(size * 10), size)
    else:
        raise ValueError(f"Tipo de vetor desconhecido: {vector_type}")

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def test_algorithms(input_file, output_file):
    sorter = SortMethods()
    
    inputs = read_input_file(input_file)

    tabela = PrettyTable()
    tabela.field_names = ["Method", "Size", "Vector Type", "Time (s)"]

    results = {}

    for method, size_str, vector_type in inputs:
        size = int(size_str)
        vector = generate_vector(size, vector_type)
        vector_copy = vector.copy()

        if method == "Insert":
            comparisons, movements, elapsed_time = sorter.insertion_sort(vector_copy)
            method_name = "Insertion Sort"
        elif method == "Select":
            comparisons, movements, elapsed_time = sorter.select_sort(vector_copy)
            method_name = "Selection Sort"
        elif method == "Shell":
            comparisons, movements, elapsed_time = sorter.shell_sort(vector_copy)
            method_name = "Shell Sort"
        elif method == "Heap":
            comparisons, movements, elapsed_time = sorter.heap_sort(vector_copy)
            method_name = "Heap Sort"
        elif method == "Merge":
            comparisons, movements, elapsed_time = sorter.merge_sort(vector_copy)
            method_name = "Merge Sort"
        else:
            raise ValueError(f"Método desconhecido: {method}")

        tabela.add_row([method_name, size, vector_type, f"{elapsed_time:.2e}"])

        if size not in results:
            results[size] = {}
        
        if method_name not in results[size]:
            results[size][method_name] = {"comparisons": 0, "movements": 0}
        
        results[size][method_name]["comparisons"] += comparisons
        results[size][method_name]["movements"] += movements

    with open(output_file, 'w') as file:
        file.write(str(tabela))

    print("\nTabela de Resultados (Tempo em segundos, notação científica):")
    print(tabela)

    for size in results:
        plot_results(results[size], size)

def plot_results(results, size):
    if not results:
        print("Nenhum resultado para plotar.")
        return

    methods = list(results.keys())
    comparisons = [results[method]["comparisons"] for method in methods]
    movements = [results[method]["movements"] for method in methods]

    x = range(len(methods))

    fig, ax = plt.subplots()
    bar_width = 0.35
    opacity = 0.8

    bars1 = ax.bar(x, comparisons, bar_width,
                   alpha=opacity, color='b',
                   label='Comparações')

    bars2 = ax.bar([p + bar_width for p in x], movements, bar_width,
                   alpha=opacity, color='r',
                   label='Movimentações')

    ax.set_xlabel('Método')
    ax.set_ylabel('Quantidade')
    ax.set_title(f'Comparações e Movimentações por Algoritmo (Tamanho: {size})')
    ax.set_xticks([p + bar_width/2 for p in x])
    ax.set_xticklabels(methods)
    ax.legend()

    plt.tight_layout()
    plt.savefig(f'questao7/algorithms_comparison_size_{size}.png')
    plt.show()

if __name__ == "__main__":
    test_algorithms('questao7/input.txt', 'questao7/output.txt')
