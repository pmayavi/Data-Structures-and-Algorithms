using System;
using System.Linq;
//Code by Pablo Maya Villegas
//8 February 2022
public class Board
{
    public int[] board;
    private int size;

    public Board(int q)
    {
        size = q;
        board = new int[q];
    }

    public Board(Board b)
    {
        size = b.size;
        board = new int[size];
        Array.Copy(b.board, 0, board, 0, size);
    }

    public bool canPlace(int c, int queen)
    {
        bool place = !board.Contains(queen);

        for (int i = c - 1; i >= 0 && place; i--)
        {
            if (queen + c == board[i] + i)
                place = false;
            else if (queen - c == board[i] - i)
                place = false;
        }
        return place;
    }
}