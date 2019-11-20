using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NumberToText
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, sum = 0, r;
            Console.Write("Enter Your Number : ");
            n = int.Parse(Console.ReadLine());
            while(n>0){
                r = n % 10;
                sum = sum * 10 + r;
                n /= 10;

            }
            n = sum;
            while(n>0){
                r = n % 10;
                switch (r) { 
                    case 1:
                        Console.Write("One\n");
                        break;
                    case 2:
                        Console.Write("Two\n");
                        break;
                    case 3:
                        Console.Write("Three\n");
                        break;
                    case 4:
                        Console.Write("Four\n");
                        break;
                    case 5:
                        Console.Write("Five\n");
                        break;
                    case 6:
                        Console.Write("Six\n");
                        break;
                    case 7:
                        Console.Write("Seven\n");
                        break;
                    case 8:
                        Console.Write("Eight\n");
                        break;
                    case 9:
                        Console.Write("Nine\n");
                        break;
                    default:
                        Console.Write("ttf");
                        break;
                        
                }
                n/=10;
            }
        }
    }
}
