using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CheckPrime
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, i, m = 0, falg = 0;
            Console.Write("Enter the number: ");
            n = int.Parse(Console.ReadLine());
            m = n / 2;
            for (i = 2; i < m; i++ ) {
                if(n%i==0){
                    Console.Write("Number is Not Prime. \n");
                    falg = 1;
                    break;
                }   
            }
            if(falg==0){
                Console.Write("Number is Prime. \n");
            }
        }
    }
}
