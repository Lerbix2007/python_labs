using System;
namespace Labs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            float numb1 = Convert.ToSingle(Console.ReadLine());
            float numb2 = Convert.ToSingle(Console.ReadLine());
            float Sum = numb1 + numb2;
            float mid = Sum / 2; //Мне было очень лень искать, как это можно сделать по другому, но 100% можно сделать через перебор массива или через for
            Console.WriteLine("Сумма= " + Sum + " | ср. арифм= " + mid);
        }
    }
}