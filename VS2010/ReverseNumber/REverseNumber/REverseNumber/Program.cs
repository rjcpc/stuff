using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace REverseNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, reverse = 0, ren;
            Console.Write("Enter Your Number: ");
            n = int.Parse(Console.ReadLine());
            while(n!=0){
                ren = n % 10;
                reverse = reverse * 10 + ren;
                n /= 10;
            }
            Console.Write("Reversed Number "+ reverse+"\n\n\n");
        }
    }
}

/*
 *Output:
 * 
 */