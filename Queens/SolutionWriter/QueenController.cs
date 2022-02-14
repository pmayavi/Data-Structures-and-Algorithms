using System;
using System.IO;
using System.Linq;
//Code by Pablo Maya Villegas
//8 February 2022
public class QueenController
{
    int size;
    //The String process is where a succesfull combination of queens is stored
    String process;

    //Constructor, recieves the size of the board or the number of queens
    //Writes a txt file with the found combinations
    public QueenController(int s)
    {
        size = s;
        process = "";
        Board board = new Board(size);
        int solution = recursive(board, 0, 1);
        Console.Write(solution);
        createFile(solution);
    }

    //Recursive method, recieves a board, the inicial index and the inicial number of queen to be tested
    public int recursive(Board board, int x, int q)
    {
        int sum = 0;
        while (x < size) //While it's inside the array
        {
            while (q <= size) //Try only queens within the range
            {
                if (board.canPlace(x, q)) //If the queen can be placed at that index
                {
                    sum += recursive(new Board(board), x, q + 1);//Recursion, the next queen tried is different
                    board.placeQueen(x, q);
                    q = 1;
                    break;
                }
                q++;
            }
            if (board.board[x] == 0) //If the number at the index is a 0, it means no queen was placed
                return sum;
            x++;
        }
        saveBoard(board);
        return sum + 1;
    }

    //Adds the succesful board to the process
    public void saveBoard(Board board)
    {
        process += board.process + "\n";
    }

    //Writes a file, flips it so that is easier to understand
    public void createFile(int solution)
    {
        process += "\n" + solution + " Possible combinations";
        process = string.Join("\n", process.Split('\r', '\n').Reverse());
        File.WriteAllText("Combinations" + size + "Queens.txt", process);
    }
}