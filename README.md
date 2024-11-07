using System;
using System.Collections;

class Program
{
    static void Main()
    {
        Console.WriteLine("Son kiriting:");
        string n = Console.ReadLine();
        int num = int.Parse(n);

        ArrayList fibonacciNumbers = new ArrayList();
        int sum = SumFibonacci(num, fibonacciNumbers);

        Console.WriteLine($"Fibonachchi sonlarining {num}-gacha bo'lgan yig'indisi: {sum}");
        Console.WriteLine("Fibonachchi sonlar:");

        foreach (int number in fibonacciNumbers)
        {
            Console.Write(number + " ");
        }
    }

    static int Fibonacci(int n)
    {
        if (n <= 0)
            return 0;
        else if (n == 1)
            return 1;
        else
            return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    static int SumFibonacci(int n, ArrayList fibonacciNumbers)
    {
        int sum = 0;

        for (int i = 0; i <= n; i++)
        {
            int fib = Fibonacci(i);
            fibonacciNumbers.Add(fib);
            sum += fib; 
        }

        return sum;
    }
}
