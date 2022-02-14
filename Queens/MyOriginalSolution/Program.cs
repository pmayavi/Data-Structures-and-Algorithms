using System;
//Code by Pablo Maya Villegas
//3 February 2022

int queens = 5;
Console.Write("Close by inputing a letter \nNumber of queens: ");

while (Int32.TryParse(Console.ReadLine(), out queens))
{
    if (queens >= 5)
    {
        Console.Write("Combinations possible: ");
        new QueenController(queens);
        Console.WriteLine("The file was created succesfully");
    }
    else Console.WriteLine("Number needs to be >= 5 ");
    Console.Write("\nNumber of queens: ");
}