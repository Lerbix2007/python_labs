using System;
namespace Labs

{
internal class Program;

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

