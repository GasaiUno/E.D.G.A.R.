using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp77
{
    class Program
    {
        static void Main(string[] args)
        {
            int menu;
            do
            {
                Mass();
                Menu(menu=EnterMenu());
                Console.WriteLine();
            } while (menu != 0);
            }
        static int SMS(int i)
        {
            Console.WriteLine("Введите значение №{0}",i);
            int a = Convert.ToInt32(Console.ReadLine());
            return a;
        }
        static void Menu(int g)
        {
            int a, b;
            int f = 1;
            int menu=g;
            switch (menu)
            {
                case 1:
                    int answer = 1;
                    do
                    {
                        a = SMS(f);
                        f++;
                        b = SMS(f);
                        Console.WriteLine("Сумма: {0}+{1}={2}", a, b, a + b);
                        Console.WriteLine("Хотите повторно выполнить операцию? 1/0");
                        answer = Convert.ToInt32(Console.ReadLine());
                        f = 1;
                    } while (answer != 0);
                    break;
                case 2:
                    a = SMS(f);
                    f++;
                    b = SMS(f);
                    Console.Write("Сумма: {0}-{1}={2}", a, b, a - b);
                    Console.ReadKey();
                    break;
                case 3:
                    int Sum = 0;
                    Console.Write("Введите n");
                    int n = Convert.ToInt32(Console.ReadLine()); ;
                    for (int j = 0; j < n; j++)
                    {
                        Sum = Sum + j;
                    }
                    Console.Write("Сумма всех чисел от 1 до {0}= {1}", n, Sum);
                    Console.ReadKey();
                    break;
                default:
                    Console.WriteLine("ERROR");
                    break;
            }
        }
        static int EnterMenu()
        {
            Console.WriteLine("1- Сумма");
            Console.WriteLine("2- Разность");
            Console.WriteLine("3- Сумма значений до n");
            Console.WriteLine("0- Выход");
            Console.Write("Ваш выбор: ");
            int menu= Convert.ToInt32(Console.ReadLine());
            return menu;
        }
        static void Mass()
        {
            int n = 3, m = 3;
            int[,] arr1 = new int[n, m];
            int[,] arr2 = new int[n, m];
            int[,] SummArr = new int[n, m];
            ReadMass(n, m, arr1);
            ReadMass(n, m, arr2);
            SumMass(n, m, arr1, arr2, SummArr);
            WriteMass(n, m, arr1);
            WriteMass(n, m, arr2);
            WriteMass(n, m, SummArr);
        }
        static void WriteMass(int n,int m,int [,]arr)
        {
            for(int k = 0; k < n; k++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.Write("{0} ",arr[k, j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
        }
        static void ReadMass(int n, int m, int[,] arr)
        {
            for (int k = 0; k < n; k++)
            {
                for (int j = 0; j < m; j++)
                {
                    arr[k, j] = Convert.ToInt32(Console.ReadLine());
                }
            }
        }
        static void SumMass(int n, int m, int [,] arr1,int [,] arr2,int [,] arr3)
        {
            for (int k = 0; k < n; k++)
            {
                for (int j = 0; j < m; j++)
                {
                    arr3[k, j] = arr1[k, j] + arr2[k, j];
                }
            }
        }
    }
}
