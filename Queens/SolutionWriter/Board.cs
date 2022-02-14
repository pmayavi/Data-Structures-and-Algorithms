using System;
using System.Linq;
//Code by Pablo Maya Villegas
//8 February 2022
public class Board
{
    //The board is saved as one array of n length
    public int[] board;
    private int size;
    //The string that saves the location a queen was placed
    public String process;

    //Constructor that recieves the number of queens
    public Board(int q)
    {
        size = q;
        process = "";
        board = new int[q];
    }

    //Constructor that copies an existing board
    public Board(Board b)
    {
        size = b.size;
        process = b.process;
        board = new int[size];
        Array.Copy(b.board, 0, board, 0, size);
    }

    //Checks if a queen can be placed at index c
    public bool canPlace(int c, int queen)
    {
        bool place = !board.Contains(queen); //If theres already a queen with that number

        for (int i = c - 1; i >= 0 && place; i--) //Cicles to previous queens
        {
            if (queen + c == board[i] + i) //If an existing queen shares diagonals
                place = false;
            if (queen - c == board[i] - i) //Using the formula of x + y and x - y == diagonals
                place = false;
        }
        return place;
    }

    //Places a queen and stores the position
    public void placeQueen(int c, int queen)
    {
        board[c] = queen;
        process += queen + " ";
    }
}