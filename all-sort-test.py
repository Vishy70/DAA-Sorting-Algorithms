import numpy as np
import time
import Algorithms
import generating
from Algorithms import Bubble_sort, Bubble_sort2, Insertion_sort, Merge_sort, Quick_sort1, Quick_sort2, Quick_sort3, Heap_sort, Radix_sort
from generating import GenerateRandom, GenerateRandomDec, GenerateRandomInc

#index-based ChooseSort
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
        print("Algo: ", sorting_functions[choice].__name__)
        sorting_functions[choice](arr)
        #print("Sorted array:", sorted_array)
    else:
        print("Invalid choice")




def TestAllSortingAlgos():
    choice = int(input("Enter 0 for your own array, 1 for a random array, 2 for an increasing array and 3 for a decreasing array: "))
    if(choice == 0):
        array_string = input("Enter elements of the array separated by spaces: ")
        arr = list(map(int, array_string.split())) 
    elif(choice == 1):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandom([arr_size])[0]
    elif(choice == 2):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandomInc([arr_size])[0]
    elif(choice == 3):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandomDec([arr_size])[0]
    else:
        print("Error! Entered an invalid input!")
        exit()
    for i in range(1,10):
        anew=arr.copy(); #to ensure that arr wont be sorted for remaining cases
        #print("Unsorted array:", anew)
        start_time = time.time()
        ChooseSort(i,anew)
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time: ", round(total_time, 6))


if __name__ == "__main__":
    TestAllSortingAlgos()
