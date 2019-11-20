using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace test23
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, r, sum = 0, temp;
            Console.Write("Enter The Number : ");
            n = int.Parse(Console.ReadLine());
            temp = n;
            while (n > 0) {
                r = n % 10;
                sum=(sum*10)+r;
                n = n / 10;
            }
            if (temp == sum)
            {
                Console.Write("Number is palindrone. \n");
            }
            else {
                Console.Write("Number is Not palindrone. \n");
            }

        }
    }
}
