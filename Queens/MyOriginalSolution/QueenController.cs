using System;
using System.IO;
using System.Linq;
//Code by Pablo Maya Villegas
//3 February 2022
public class QueenController
{
    //The String process is where a succesfull combination of queens is stored
    int size;
    String process;

    //Constructor, recieves the size of the board or the number of queens
    //Writes a txt file with the found combinations
    public QueenController(int s)
    {
        size = s;
        process = "";
        Board board = new Board(size);
        Console.WriteLine(recursive(board));
        process = string.Join("\n", process.Split('\r', '\n').Reverse());
        File.WriteAllText("Combinations" + s + "Queens.txt", process);
    }

    //Recursive class that recieves a board
    public int recursive(Board board)
    {
        //The 'placed' variable is used to check if a queen was placed in the current line
        bool placed = false;
        int sum = 0;

        //Moves to the next square, if  false then it's the end of the board
        while (board.moveCursorNext())
        {
            //Checks if the current square is empty to place a queen
            if (board.checkCurrent())
            {
                //When a queen is placed the tree splits to check if another queen can be placed at the same line
                sum += newBranch(board);
                board.placeQueen();
                placed = true;
                board.moveCursorDown();
            }
            //If it reaches the end of line and no queen was placed, then the search is terminated
            if (board.getCursor() % size == 0 && !placed)
                break;
        }

        //If all queens were placed, the branch was succesfull and adds one to the counter
        if (board.getQueens() == 0)
        {
            process += board.getProcess() + "\n";
            return (1 + sum);
        }
        return sum;
    }

    //Creates a clone of the board to create a branch
    public int newBranch(Board board)
    {
        //If it's at the end of the line it doesn't split
        if (board.getCursor() % size != 0)
        {
            Board boardClone = new Board(board);
            return recursive(boardClone);
        }
        return 0;
    }
}

