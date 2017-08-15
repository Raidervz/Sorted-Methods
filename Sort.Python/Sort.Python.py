import sys 
from methods import methods
from exampledata import exampledata
from array import array

def main():

    result = methods.VisualSort(exampledata.Data_1000)
    print("Visual Sort\n")
    displayArray(result)

    pass

def displayArray(arreglo=array('i')):
    print("[ ")
    for x in arreglo:
        print(arreglo[x] + ", ")
    print("]")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
