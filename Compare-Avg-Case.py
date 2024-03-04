import numpy as np
import time
import matplotlib.pyplot as plt
import Algorithms
import generating
import plotter
from Algorithms import Bubble_sort, Bubble_sort2, Insertion_sort, Merge_sort, Quick_sort1, Quick_sort2, Quick_sort3, Heap_sort, Radix_sort
from generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc
from plotter import plot_results

#Function name based ChooseSort
def ChooseSort(choice, arr):
    sorting_functions = {
        1: Bubble_sort,
        2: Bubble_sort2,
        3: Insertion_sort,
        4: Merge_sort,
        5: Quick_sort1,
        6: Quick_sort2,
        7: Quick_sort3,
        8: Heap_sort,
        9: Radix_sort
    }

    if choice in sorting_functions:
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")


def CompareAverageCase():
    array_sizes = list(range(1000, 2001, 100))
    sorting_algorithms = [
        Bubble_sort,
        Bubble_sort2,
        Insertion_sort,
        Merge_sort,
        Quick_sort3,
        Heap_sort,
        Radix_sort
    ]

    average_times = {sorting_algo.__name__: [] for sorting_algo in sorting_algorithms}

    random_arrays = GenerateRandom(array_sizes)  # Generate random arrays

    for size in array_sizes:
        for algo in sorting_algorithms:
            total_time = 0
            for i in range(30):
                random_array = random_arrays[30*(size//100-1)+i]  # Get the corresponding random array
                arr_copy = random_array.copy()  # Use copy of the random array for each algorithm
                start_time = time.time()
                ChooseSort(sorting_algorithms.index(algo) + 1, arr_copy)
                end_time = time.time()
                total_time += end_time - start_time
            average_time = total_time / 30
            average_times[algo.__name__].append(average_time)

    return sorting_algorithms, average_times, array_sizes


if __name__ == "__main__":
    sorting_algorithms, average_times, array_sizes = CompareAverageCase()
    plot_results(sorting_algorithms, average_times, array_sizes)
