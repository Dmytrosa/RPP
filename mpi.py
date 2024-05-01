from mpi4py import MPI
import numpy as np
import time

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
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    MAX = 10000

    arr = None

    if rank == 0:
        all_numbers = np.arange(1, MAX+1)
        np.random.shuffle(all_numbers)
        arr = np.array_split(all_numbers, size)

    start = time.time()

    local_arr = comm.scatter(arr, root=0)

    local_arr.sort()

    sorted_arr = comm.gather(local_arr, root=0)

    if rank == 0:
        sorted_arr = np.concatenate(sorted_arr)
        mergeSort(sorted_arr)
        end = time.time()

        print("Array Size: {}, Processes: {}, Time Taken: {} seconds".format(MAX, size, end - start))
        
        np.savetxt('sorted_numbers.txt', sorted_arr, fmt='%d', delimiter='\n', newline='\n', comments='')

if __name__ == "__main__":
    main()
