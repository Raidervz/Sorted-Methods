using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort
{
    public class Methods
    {

        public int[] VisualSort(int[] arreglo)
        {
            int[] ArregloActual = arreglo.ToArray();

            int[] ArregloNuevo = new int[arreglo.Length];

            int ArregloTotal = arreglo.Length;

            int marked = 0;

            while (marked != ArregloTotal)
            {
                int maxed = -1;
                int maxedIndex = -1;
                for (int i = 0; i < ArregloActual.Length; i++)
                {
                    if (ArregloActual[i] > maxed)
                    {
                        maxed = ArregloActual[i];
                        maxedIndex = i;
                    }
                }

                ArregloNuevo[ArregloTotal - marked - 1] = maxed;
                ArregloActual[maxedIndex] = -1;

                marked++;
            }

            return ArregloNuevo;
        }

        public int[] SelectionSort(int[] arreglo)
        {
            int[] responce = new int[arreglo.Length];

            responce = arreglo.ToArray();

            for (int i = 0; i <= responce.Length - 1; i++)
            {
                int MaxValueIndex = i;
                for (int j = i + 1; j <= responce.Length - 1; j++)
                {
                    if (responce[j] < responce[MaxValueIndex])
                    {
                        MaxValueIndex = j;
                    }
                }
                //Guardar el Valor Actual 
                int actualValue = responce[i];

                //Reemplazarlo con el Valor menor
                responce[i] = responce[MaxValueIndex];

                //Poner el Valor Actual en la posicion del Valor Menor
                responce[MaxValueIndex] = actualValue;

            }

            return responce;
        }

        public int[] BubbleSort(int[] arreglo)
        {
            int[] responce = new int[arreglo.Length];

            responce = arreglo.ToArray();

            for (int i = 1; i < responce.Length - 1; i++)
            {
                int stopper = 0;
                for (int j = 0; j <= responce.Length - i - 1; j++)
                {
                    if (responce[j] > responce[j + 1])
                    {
                        int actualValue = responce[j];
                        int nextValue = responce[j + 1];

                        responce[j] = nextValue;
                        responce[j + 1] = actualValue;

                        stopper = 1;
                    }
                }
                if (stopper == 0) break;
            }

            return responce;
        }

        public int[] InsertionSort(int[] arreglo)
        {
            int[] responce = new int[arreglo.Length];

            responce = arreglo.ToArray();

            for (int i = 1; i < responce.Length; i++)
            {
                int indexA = i;
                int indexB = i - 1;

                while (responce[indexA] < responce[indexB] && indexB > -1)
                {
                    int actualValue = responce[indexA];
                    int nextValue = responce[indexB];

                    responce[indexA] = nextValue;
                    responce[indexB] = actualValue;

                    indexA--;
                    if (indexB - 1 == -1)
                    {
                        break;
                    }
                    else
                    {
                        indexB--;
                    }
                }
            }

            return responce;
        }

        public int[] MergeSort(int[] arreglo)
        {
            int[] responce = new int[arreglo.Length];
            responce = arreglo.ToArray();

            if (arreglo.Length < 2)
            {
                return responce;
            }
            else
            {
                //Split Array + / - 50%
                int splitNum = responce.Length / 2;
                int[] arrayL = new int[splitNum];
                int[] arrayR = new int[responce.Length - splitNum];

                for (int i = 0; i < splitNum; i++)
                {
                    arrayL[i] = responce[i];
                }

                for (int i = splitNum; i < responce.Length; i++)
                {
                    arrayR[i - splitNum] = responce[i];
                }

                //Sort Splited array parts Using any of the other methods
                arrayL = MergeSort(arrayL);
                arrayR = MergeSort(arrayR);

                //Merge splited parts to main array
                int arrayLIndex = 0;
                int arrayRIndex = 0;
                int responceIndex = 0;

                while (arrayLIndex < arrayL.Length && arrayRIndex < arrayR.Length)
                {
                    if (arrayL[arrayLIndex] <= arrayR[arrayRIndex])
                    {
                        responce[responceIndex] = arrayL[arrayLIndex];
                        arrayLIndex++;
                    }
                    else
                    {
                        responce[responceIndex] = arrayR[arrayRIndex];
                        arrayRIndex++;
                    }
                    responceIndex++;
                }

                while (arrayLIndex < arrayL.Length)
                {
                    responce[responceIndex] = arrayL[arrayLIndex];
                    arrayLIndex++;
                    responceIndex++;
                }

                while (arrayRIndex < arrayR.Length)
                {
                    responce[responceIndex] = arrayR[arrayRIndex];
                    arrayRIndex++;
                    responceIndex++;
                }
            }

            return responce;
        }

        public int QuickSort(int[] arreglo, int startIndex, int endIndex)
        {
            int correctSortElementIndex = startIndex;

            if (startIndex < endIndex)
            {
                int sortElement = arreglo[endIndex];

                for (int i = startIndex; i < endIndex; i++)
                {
                    if (arreglo[i] <= sortElement)
                    {
                        int actualValue = arreglo[i];
                        int newValue = arreglo[correctSortElementIndex];

                        arreglo[i] = newValue;
                        arreglo[correctSortElementIndex] = actualValue;
                        correctSortElementIndex++;
                    }
                }

                int initialSortElementIndex = arreglo[endIndex];
                int actualSortElementIndex = arreglo[correctSortElementIndex];

                arreglo[endIndex] = actualSortElementIndex;
                arreglo[correctSortElementIndex] = initialSortElementIndex;

                QuickSort(arreglo, startIndex, correctSortElementIndex - 1);
                QuickSort(arreglo, correctSortElementIndex + 1, endIndex);

            }
            return correctSortElementIndex;

        }
    }
}
