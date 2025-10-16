
using System;
namespace Labs
{
    internal class Program
    {
        static void Main(string[] args)
        {

            string name = "Иванов Иван Иванович";
            Console.WriteLine($"ФИО: {name}");
            int length = name.Length;
            Console.WriteLine($"Длина (символов): {length}");

            string result = " ";
            for (int i = 0; i < name.Length; i++)
            {
                
                if (i == 0 || name[i - 1] == ' ')
                {
                    result += name[i];
                }
            }

            Console.WriteLine("Краткое ФИО: "+result);



        }
    }
}