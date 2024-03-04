import numpy as np
import time
import matplotlib.pyplot as plt

def plot_results(sorting_algorithms, average_times, array_sizes):

    plt.figure(figsize=(12, 8))

    # Plot with normal scale
    plt.subplot(2, 1, 1)
    for algo in sorting_algorithms:
        name = algo.__name__
        plt.plot(array_sizes, average_times[name], marker='o', label=name)
    plt.title('Average Sorting Time vs Array Size (Normal Scale)')
    plt.xlabel('Array Size')
    plt.ylabel('Average Sorting Time (seconds)')
    plt.grid(True)
    plt.legend()

    # Plot with logarithmic scale
    plt.subplot(2, 1, 2)
    for algo in sorting_algorithms:
        name = algo.__name__
        plt.plot(array_sizes, average_times[name], marker='o', label=name)
    plt.title('Average Sorting Time vs Array Size (Logarithmic Scale)')
    plt.xlabel('Array Size')
    plt.ylabel('Average Sorting Time (seconds)')
    plt.grid(True)
    plt.xscale('log')  # Set logarithmic scale for array size
    plt.legend()

    plt.tight_layout()
    plt.show()