using System;
using System.Linq;
//Code by Pablo Maya Villegas
//3 February 2022
public class Board
{
    //The board is saved as one array
    private int[] board;
    //Size is the length of one side, totalSize is the number of squares 
    //Cursor is the current square and queens is the number that need to be placed 
    private int size, totalSize, cursor, queens;
    //process saves the number of the squares a queen was placed
    private String process;

    //Constructor that recieves the size
    public Board(int s)
    {
        size = s;
        queens = s;
        cursor = 0;
        process = "";
        totalSize = (s * s) + 1;
        board = Enumerable.Repeat(0, totalSize).ToArray();
    }

    //Constructor that copies an existing board
    public Board(Board b)
    {
        size = b.size;
        queens = b.queens;
        cursor = b.cursor;
        process = b.process;
        totalSize = b.totalSize;
        board = new int[totalSize];
        Array.Copy(b.board, 0, board, 0, totalSize);
    }

    //Checks if the current square is empty
    public bool checkCurrent()
    {
        if (board[cursor] == 0)
            return true;
        else return false;
    }

    //Moves to the next square, if it's the end of the board returns false
    public bool moveCursorNext()
    {
        cursor += 1;
        if (cursor == totalSize)
            return false;
        else return true;
    }
    //Moves to the first square of the next line
    public void moveCursorDown()
    {
        if (cursor % size != 0)
            cursor += size - (cursor % size);
    }

    //Places a queen and marks the squares in her range
    public void placeQueen()
    {
        --queens;
        process += 1 + ((cursor - 1) % size) + "  ";
        //Marks the squares to the right of the queen
        for (int i = cursor; i < totalSize; i++)
        {
            board[i] = 1;
            if (i % size == 0)
                break;
        }
        //Marks the squares below the queen and diagonaly to her
        //Stops if the diagonal reaches the side of the board
        int diagonals = 1;
        for (int i = cursor + size; i <= totalSize - 1; i += size)
        {
            board[i] = 1;
            if (i % size != 0 && diagonals <= size - (i % size))
                board[i + diagonals] = 1;
            if (i % size != 1 && diagonals <= (i - 1) % size)
                board[i - diagonals] = 1;
            diagonals++;
        }
    }

    public int getQueens()
    {
        return queens;
    }

    public int getCursor()
    {
        return cursor;
    }

    public String getProcess()
    {
        return process;
    }
}