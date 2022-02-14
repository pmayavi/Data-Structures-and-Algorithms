using System;
using System.IO;
using System.Linq;
//Code by Pablo Maya Villegas
//8 February 2022
public class QueenController{
    int size;

    public QueenController(int s){
        size = s;
        Board board = new Board(size);
        int solution = recursive(board, 0, 1);
        Console.Write(solution);
    }

    public int recursive(Board board, int x, int q){
        int sum = 0;
        while (x < size){
            while (q <= size){
                if (board.canPlace(x, q)){
                    sum += recursive(new Board(board), x, q + 1);
                    board.board[x] = q;
                    q = 1;
                    break;
                }
                q++;
            }
            if (board.board[x] == 0)
                return sum;
            x++;
        }
        return sum + 1;
    }
}