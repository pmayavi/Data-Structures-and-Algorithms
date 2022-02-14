using System;
//Code by Pablo Maya Villegas
//8 February 2022

int queens = 5;
Console.Write("Close by inputing a letter \n");
Console.Write("Automate the process by inputing 0 \n\nNumber of queens: ");

while (Int32.TryParse(Console.ReadLine(), out queens))
{
    if (queens >= 5)
    {
        Console.Write("Combinations possible: ");
        new QueenController(queens);
        Console.WriteLine("\nThe file was created succesfully");
    }
    else if (queens == 0)
    {
        Console.Write("\nWhen to stop? ");
        int stop = 0;
        Int32.TryParse(Console.ReadLine(), out stop);
        for (int i = 5; i <= stop; i++)
        {
            Console.Write("\n" + i + " = ");
            new QueenController(i);
        }
    }
    else Console.WriteLine("Number needs to be >= 5 ");
    Console.Write("\nNumber of queens: ");
}