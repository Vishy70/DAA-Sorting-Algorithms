import numpy as np
import time
import matplotlib.pyplot as plt
import Algorithms
import generator.generating as generating
import plotter
from Algorithms import Bubble_sort, Bubble_sort2, Insertion_sort, Merge_sort, Quick_sort1, Quick_sort2, Quick_sort3, Heap_sort, Radix_sort
from generator.generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc
from plotter import plot_results




#Function name based ChooseSort
def ChooseSort(choice, arr):
    sorting_functions = {
        #2: Bubble_sort2
        #3: Insertion_sort,
        1: Merge_sort,
        #2: Quick_sort1,
        #3: Quick_sort2,
        2: Quick_sort3,
        3: Heap_sort,
        4: Radix_sort
    }

    if choice in sorting_functions:
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")


def CompareAverageCase(iterations):
    array_sizes = list(range(1000, 10001, 100))
    sorting_algorithms = [
        #Bubble_sort2,
        #Insertion_sort,
        Merge_sort,
        #Quick_sort1,
        #Quick_sort2,
        Quick_sort3,
        Heap_sort,
        Radix_sort
    ]

    average_times = {sorting_algo.__name__: [] for sorting_algo in sorting_algorithms}

    #random_arrays = GenerateRandom(array_sizes)  # Generate random arrays

    for index, size in enumerate(array_sizes):
        random_array = GenerateRandom(size)
        for algo in sorting_algorithms:
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
    sorting_algorithms, average_times, array_sizes = CompareAverageCase(iterations)
    plot_results(sorting_algorithms, average_times, array_sizes)
