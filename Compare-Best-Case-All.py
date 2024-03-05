import numpy as np
import time
import matplotlib.pyplot as plt
import Algorithms
import plotter
from Algorithms import Bubble_sort, Insertion_sort, Merge_sort, Quick_sort3, Heap_sort, Radix_sort
from generator.generating import GenerateRandom, GenerateRandomInc, GenerateRandomDec
from generator.gen_bubble import Generate_Bubble_Best
from generator.gen_heap import Generate_Heap_Best
from generator.gen_insertion import Generate_Insertion_Best
from generator.gen_merge import Generate_Merge_Best
from generator.gen_quick3 import Generate_Quick3_Best
from generator.gen_radix import Generate_Radix_Best
from plotter import plot_results 




#Function name based ChooseSort
def ChooseSort(choice, arr):
    sorting_functions = {
        1: Bubble_sort,
        2: Insertion_sort,
        3: Merge_sort,
        4: Quick_sort3,
        5: Heap_sort,
        6: Radix_sort
    }

    if choice in sorting_functions:
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")


def CompareBestCase(iterations):
    array_sizes = list(range(1000, 10001, 100))
    sorting_algorithms = [
        Bubble_sort,
        Insertion_sort,
        Merge_sort,
        Quick_sort3,
        Heap_sort,
        Radix_sort
    ]
    gen_algorithms = [
        Generate_Bubble_Best,
        Generate_Insertion_Best,
        Generate_Merge_Best,
        Generate_Quick3_Best,
        Generate_Heap_Best,
        Generate_Radix_Best
    ]

    average_times = {sorting_algo.__name__: [] for sorting_algo in sorting_algorithms}

    for index, algo in enumerate(sorting_algorithms):
        for size in array_sizes:
            random_array = gen_algorithms[index](size)
            total_time = 0
            for i in range(iterations):
                #random_array = random_arrays[index]
                arr_copy = random_array.copy()  # Use copy of the random array for each algorithm
                start_time = time.time()
                ChooseSort(sorting_algorithms.index(algo) + 1, arr_copy)
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / iterations
            average_times[algo.__name__].append(average_time)

    return sorting_algorithms, average_times, array_sizes


if __name__ == "__main__":
    iterations = 10
    sorting_algorithms, average_times, array_sizes = CompareBestCase(iterations)
    plot_results(sorting_algorithms, average_times, array_sizes)
