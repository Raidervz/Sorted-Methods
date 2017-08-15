from array import array

class methods(object):
    """description of class"""

    def VisualSort(arreglo=[]):
        arregloActual = arreglo
        arregloNuevo = [None] * len(arreglo)
        arregloTotal = len(arreglo)
        marked = 0;
        while marked != arregloTotal:
            maxed = -1
            maxedIndex = -1
            for i in range(0, len(arregloActual) - 1):
                if arregloActual[i] > maxed :
                    maxed = arregloActual[i];
                    maxedIndex += 1

            arregloNuevo[arregloTotal - marked - 1] = maxed
            arregloActual[maxedIndex] = -1;

            marked += 1

        return arregloNuevo
    


