import numpy as np
import time
import matplotlib.pyplot as plt

#Bubble Sort
def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Bubble Sort with pruning
def Bubble_sort2(arr):
    n = len(arr)
    for i in range(n):
        sorted = True  
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False  # change means no pruning
        if sorted:  #pruning check
            break
        
#Insertion Sort
def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#Merge Sort
def Merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 #integer division, since python
        L = arr[:mid]
        R = arr[mid:]

        Merge_sort(L)
        Merge_sort(R)

        i = 0; j = 0; k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def Quick_sort1(arr):
    #Quick Sort with pivot = low!
    def quick_sort_1(arr, low, high):
        if low < high:
            pivot_index_fake = np.random.randint(low, high + 1)
            pivot = arr[low]
            i = low
            j = high
            while i < j:
                while i <= high and arr[i] <= pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
            
            quick_sort_1(arr, low, j - 1)
            quick_sort_1(arr, j + 1, high)

    quick_sort_1(arr, 0, len(arr) - 1)

def Quick_sort2(arr):
    #Quick Sort with pivot = random!
    def quick_sort_2(arr, low, high):
        if low < high:
            pivot_index = np.random.randint(low, high + 1)
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
            pivot = arr[low]
            i = low + 1
            for j in range(low + 1, high + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[low], arr[i - 1] = arr[i - 1], arr[low]
            
            quick_sort_2(arr, low, i - 2)
            quick_sort_2(arr, i, high)

    quick_sort_2(arr, 0, len(arr) - 1)

def Quick_sort3(arr):
    #Median of three helper for better pivot!
    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            if arr[mid] > arr[high]:
                return mid
            elif arr[low] > arr[high]:
                return high
            else:
                return low
        else:
            if arr[low] > arr[high]:
                return low
            elif arr[mid] > arr[high]:
                return high
            else:
                return mid
    
    #Quick sort with pivot = median of 3
    def quick_sort_3(arr, low, high):
        if low < high:
            pivot_index_fake = np.random.randint(low, high + 1)
            pivot_index = median_of_three(arr, low, high)
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
            pivot = arr[low]
            i = low
            j = high
            while i < j:
                while i <= high and arr[i] <= pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
            
            quick_sort_3(arr, low, j - 1)
            quick_sort_3(arr, j + 1, high)

    quick_sort_3(arr, 0, len(arr) - 1)


def Heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2     

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)



def Radix_sort(arr):
    def counting_sort(arr, exp):
        output = [0] * len(arr)
        count = [0] * 10

        for i in range(len(arr)):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(len(arr)):
            arr[i] = output[i]

    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

