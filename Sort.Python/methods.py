class methods(object):
    """description of class"""

    def VisualSort(arreglo=[]):
        arregloActual = [num for num in arreglo]
        arregloNuevo = [None] * len(arreglo)
        arregloTotal = len(arreglo)
        marked = 0
        while marked != arregloTotal:
            maxed = -1
            maxedIndex = -1
            for i in range(0, len(arregloActual) - 1):
                if arregloActual[i] > maxed :
                    maxed = arregloActual[i]
                    maxedIndex = i

            arregloNuevo[arregloTotal - marked - 1] = maxed
            arregloActual[maxedIndex] = -1

            marked += 1

        return arregloNuevo

    def SelectionSort(arreglo=[]):
        responce = [num for num in arreglo]

        for i in range(0, len(responce)):
            MaxValueIndex = i
            for j in range((i + 1), (len(responce))):
                if responce[j] < responce[MaxValueIndex]:
                    MaxValueIndex = j;

            actualValue = responce[i]
            responce[i] = responce[MaxValueIndex]
            responce[MaxValueIndex] = actualValue

        return responce

    def BubbleSort(arreglo=[]):
        responce = [num for num in arreglo]

        for i in range(1, len(responce)):
            stopper = 0
            for j in range(0, (len(responce) - i )):
                if responce[j] > responce[j + 1]:
                    actualValue = responce[j]
                    nextValue = responce[j + 1]

                    responce[j] = nextValue
                    responce[j + 1] = actualValue

                    stopper = 1
            
            if stopper == 0:
                break

        return responce

    def InsertionSort(arreglo=[]):
        responce = [num for num in arreglo]

        for i in range(1, len(responce)):
            indexA = i
            indexB = i - 1

            while (responce[indexA] < responce[indexB]) & (indexB > -1):
                actualValue = responce[indexA]
                nextValue = responce[indexB]

                responce[indexA] = nextValue
                responce[indexB] = actualValue
    
                indexA -= 1
                if indexB -1 == -1:
                    break
                else:
                    indexB -= 1;

        return responce    

    def MergeSort(arreglo=[]):
        responce = [num for num in arreglo]

        if len(arreglo) < 2:
            return responce
        else:
            splitNum = int(len(responce) / 2)
            arrayL = [None] * splitNum
            arrayR = [None] * (len(responce) - splitNum)

            for x in range(0, splitNum):
                arrayL[x] = responce[x]

            for x in range(splitNum, len(responce)):
                arrayR[x - splitNum] = responce[x] 
    
            arrayL = methods.MergeSort(arrayL)
            arrayR = methods.MergeSort(arrayR)

            arrayLIndex = 0
            arrayRIndex = 0
            responceIndex = 0

            while (arrayLIndex < len(arrayL)) & (arrayRIndex < len(arrayR)):
                if arrayL[arrayLIndex] <= arrayR[arrayRIndex]:
                    responce[responceIndex] = arrayL[arrayLIndex]
                    arrayLIndex += 1
                else:
                    responce[responceIndex] = arrayR[arrayRIndex];
                    arrayRIndex += 1

                responceIndex += 1
    
            while arrayLIndex < len(arrayL):
                responce[responceIndex] = arrayL[arrayLIndex]
                arrayLIndex += 1
                responceIndex += 1

            while arrayRIndex < len(arrayR):
                responce[responceIndex] = arrayR[arrayRIndex];
                arrayRIndex += 1
                responceIndex += 1


        return responce

    def QuickSort(arreglo: [], startIndex: int, endIndex: int ):

        correctSortElementIndex = startIndex

        if startIndex < endIndex:
            sortElement = arreglo[endIndex]

            for i in range(startIndex, endIndex):
                if arreglo[i] <= sortElement:
                    actualValue = arreglo[i]
                    newValue = arreglo[correctSortElementIndex]

                    arreglo[i] = newValue
                    arreglo[correctSortElementIndex] = actualValue
                    correctSortElementIndex += 1

            initialSortElementIndex = arreglo[endIndex]
            actualSortElementIndex = arreglo[correctSortElementIndex]

            arreglo[endIndex] = actualSortElementIndex
            arreglo[correctSortElementIndex] = initialSortElementIndex

            methods.QuickSort(arreglo, startIndex, correctSortElementIndex - 1)
            methods.QuickSort(arreglo, correctSortElementIndex + 1, endIndex)

        return correctSortElementIndex

    
    
    
        
    