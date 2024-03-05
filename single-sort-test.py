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
    else:
        print("Invalid choice")



def SortAny():
    choice1 = int(input("Enter 0 for your own array, 1 for a random array, 2 for an increasing array and 3 for a decreasing array: "))
    if(choice1 == 0):
        array_string = input("Enter elements of the array separated by spaces: ")
        arr = list(map(int, array_string.split())) 
    elif(choice1 == 1):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandom([arr_size])[0]
    elif(choice1 == 2):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandomInc([arr_size])[0]
    elif(choice1 == 3):
        arr_size = int(input("Enter size of array: "))
        arr = GenerateRandomDec([arr_size])[0]
    else:
        print("Error! Entered an invalid input!")
        exit()  
    print("Menu:\n1.Bubble Sort\n2.BubbleSort2\n3.InsertionSort\n4.MergeSort\n5.QuickSort1\n6.QuickSort2\n7.QuickSort3\n8.HeapSort\n9.RadixSort")
    choice2 = int(input("Enter choice:"))
    start_time = time.time()
    ChooseSort(choice2,arr)
    end_time = time.time()
    total_time = end_time - start_time
    print("Total time: ", round(total_time, 6))

if __name__ == "__main__":
    SortAny()



