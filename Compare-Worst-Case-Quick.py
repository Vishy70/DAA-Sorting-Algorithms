import numpy as np
import time
import matplotlib.pyplot as plt
import Algorithms
import plotter
from Algorithms import Quick_sort1, Quick_sort2, Quick_sort3
from generator.gen_quick1 import Generate_Quick1_Worst
from generator.gen_quick2 import Generate_Quick2_Worst
from generator.gen_quick3 import Generate_Quick3_Worst
from plotter import plot_results 




#Function name based ChooseSort
def ChooseSort(choice, arr):
    sorting_functions = {
        1: Quick_sort1,
        2: Quick_sort2,
        3: Quick_sort3,
    }

    if choice in sorting_functions:
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")


def CompareWorstCase(iterations):
    array_sizes = list(range(10, 1001, 25))
    sorting_algorithms = [
        Quick_sort1,
        Quick_sort2,
        Quick_sort3,
    ]
    gen_algorithms = [
        Generate_Quick1_Worst,
        Generate_Quick2_Worst,
        Generate_Quick3_Worst
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
    sorting_algorithms, average_times, array_sizes = CompareWorstCase(iterations)
    plot_results(sorting_algorithms, average_times, array_sizes)
