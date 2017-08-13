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
    }
}
