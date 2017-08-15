import sys 
from methods import methods
from exampledata import exampledata
from time import time

def main():

    show = False

    stopWatchStart = time()
    result = methods.VisualSort(exampledata.Data_1000)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Visual Sort")
    if show:
        displayArray(result)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()

    stopWatchStart = time()
    result = methods.SelectionSort(exampledata.Data_1000)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Selection Sort")
    if show:
        displayArray(result)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()

    stopWatchStart = time()
    result = methods.BubbleSort(exampledata.Data_1000)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Bubble Sort")
    if show:
        displayArray(result)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()

    stopWatchStart = time()
    result = methods.InsertionSort(exampledata.Data_1000)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Insertion Sort")
    if show:
        displayArray(result)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()

    stopWatchStart = time()
    result = methods.MergeSort(exampledata.Data_1000)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Merge Sort")
    if show:
        displayArray(result)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()

    localExampleData = [num for num in exampledata.Data_1000]
    stopWatchStart = time()
    result = methods.QuickSort(localExampleData, 0, len(localExampleData) -1)
    stopWatchEnd = time()
    stopWatchDifference = stopWatchEnd - stopWatchStart
    print("Quick Sort")
    if show:
        displayArray(localExampleData)
    print("Time elapsed: {0}".format(stopWatchDifference))
    print()



    input()


def displayArray(arreglo=[]):
    print("[ ")
    for x in range(0, len(arreglo)):
        print("{0}, ".format(arreglo[x]), end='')
    print("]")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
