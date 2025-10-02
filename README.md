Задание 1
```c#
using System;
namespace Labs;

internal class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("напиши свое имя");
        string name = Console.ReadLine();
        Console.WriteLine("теперь напиши возраст");
        int old = Convert.ToInt32(Console.ReadLine());
        if (string.IsNullOrWhiteSpace(name))
        {
            Console.WriteLine("попробуй еще раз");

        }
        else if (old == null)
        {
            Console.WriteLine("попробуй еще раз");

        }
        else;
        Console.WriteLine($"тебя зовут {name}! Через год тебе будет {++old}");


    }
}



```
![alt text](images/lab01/ex01.jpg)

Задание 2
```c#
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
```
[text](src/lab01/ex02)
![alt text](images/lab01/ex02.png)

Задание 3
```c#
using System;
namespace Labs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("введите минуты, они будут переконвертированны в часы и минуты");
            int min = int.Parse(Console.ReadLine());
            int hours = min / 60;
            int minutes = min - (hours * 60);
            Console.WriteLine(hours + ":" + minutes);

        }
    }
}
```
![alt text](images/lab01/ex03.png)

Задание 4
```c#
using System;
namespace Labs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Цена на продукт");
            int price = int.Parse(Console.ReadLine());
            if (price <= 0)
            {
                Console.WriteLine("Слишком низкая цена");
                return;
            }
            Console.WriteLine("Введите желаемую скидку");
            int discount = int.Parse(Console.ReadLine());
            if (discount <= 0)
            {
                Console.WriteLine("Скидка меньше 0 или равна 0, работашь в убыток");
                return;
            }

            else if (discount >= 50)
            {
                Console.WriteLine("Ну ты палку то не перегибай");
                return;
            };
            double Vat = 1.2;
            double Base = price * (1 - (discount / 100.0));
            double total = Base * Vat;
            Console.WriteLine("И того к оплате: "+ total+"$");
        }

    }
}

```
![alt text](images/lab01/ex04.png)
![alt text](images/lab01/ex04(1).png)

Задание 5
```c#

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
```
![alt text](images/lab01/ex05.png)

Лабораторная работа 2
Задание 1
```c#

using System;
namespace Labs
  {
    internal class Program

    {
        static int[] CombineArrays(params int[][] arrays)
        {
            List<int> result = new List<int>();
            foreach (int[] ArrayNew in arrays)
            {
                result.AddRange(ArrayNew);
            }
            return result.ToArray();
        }
        static void Main(string[] args)
        {
            //1
            int[] array1 = {2,5,16,12};
            Console.WriteLine($"изначальный массив 1: {string.Join(",", array1)} ");
            Console.WriteLine($" мин: {array1.Min()}, макс: {array1.Max()}");
            //2
            int[] array2 = {30,18,1,0};
            Console.WriteLine($"изначальный массив 2: {string.Join(",", array2)} ");
            int[] sorted = new int[array2.Length];
            Array.Copy(array2, sorted, array2.Length);
            Array.Sort(sorted);
            Console.WriteLine($"отсортированный по возр. массив: [{string.Join(", ", sorted)}]");
            //3
            int[] nullarray = { };
            int[] combined = CombineArrays(array1, nullarray, sorted);
            Console.WriteLine($"Общий массив: [{string.Join(", ", combined)}]");
            
        }

    }
  }

```
![alt text](images/lab02/ex1.png)
