import random
import time

def generate_random_array(size, max_value):
    return [random.randint(0, max_value) for _ in range(size)]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

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

def main():
    MAX = 10000
    MAX_VALUE = 10000

    arr = generate_random_array(MAX, MAX_VALUE)

    start = time.time()

    mergeSort(arr)

    end = time.time()


    print("Array Size: {}, Time Taken: {} seconds".format(MAX, end - start))

if __name__ == "__main__":
    main()
