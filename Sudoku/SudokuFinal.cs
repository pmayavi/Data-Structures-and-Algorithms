public class Sudoku
{
    private int sy;
    private int sx;
    private int syx;
    private List<int>[,] sudoku;
    private int[,] mat;
    private Random rand;
    private bool morethantwo;


    public Sudoku()
    {
        morethantwo = false;
        sudoku = new List<int>[1, 1];
        mat = new int[1, 1];
        rand = new Random();
    }

    public void read(string filedir)
    {
        string text = System.IO.File.ReadAllText(filedir + ".txt");
        int count = 0;
        int log = 0;

        string size = text.Substring(0, text.IndexOf('\n'));
        if (size.Contains("x"))
        {
            string[] s = size.Split('x');
            sx = Convert.ToInt32(s[0]);
            sy = Convert.ToInt32(s[1]);
        }
        else
            sx = sy = Convert.ToInt32(size);
        syx = sx * sy;
        int[] splittedLine = new int[syx * syx];
        log = syx.ToString().Length;
        sudoku = new List<int>[syx, syx];
        mat = new int[syx, syx];


        string str = "";
        text = text.Substring(text.IndexOf('\n') + 1);
        text = text.Replace("\n", string.Empty);
        text = text.Replace("\r", string.Empty);

        for (int i = 0; i < text.Length; i++)
        {
            str += text[i];
            if ((i + 1) % log == 0)
            {
                if (str.Contains("-"))
                    splittedLine[i / log] = 0;
                else
                    splittedLine[i / log] = Convert.ToInt32(str);
                str = "";
            }
        }

        foreach (int n in splittedLine)
        {
            sudoku[count / syx, count % syx] = new List<int>();
            sudoku[count / syx, count % syx].Add(n);
            count++;
        }
    }

    public void newBoard(int SY, int SX)
    {
        sy = SY;
        sx = SX;
        syx = sy * sx;
        int cycle = 1;
        List<List<List<int>>> newSudoku = new List<List<List<int>>>();
        List<List<int>> square = new List<List<int>>();
        int rowC = 0;
        int point = 1;
        while (rowC < sx)
        {
            List<int> row = Enumerable.Range(point, sx).ToList();
            point += sx;
            rowC += 1;
            square.Add(row);
        }
        newSudoku.Add(square);

        while (cycle < syx)
        {
            rowC = 0;
            point = 0;
            List<List<int>> lastsquare = new List<List<int>>();
            foreach (List<int> row in newSudoku[newSudoku.Count - 1])
                lastsquare.Add(new List<int>(row));

            if (cycle % sx == 0)
            {
                while (rowC < sx)
                {
                    List<int> row = lastsquare[point];
                    point += 1;
                    int firstElement = row[0];
                    row.RemoveAt(0);
                    row.Add(firstElement);
                    rowC += 1;
                }
            }
            List<int> FirstRow = lastsquare[0];
            lastsquare.RemoveAt(0);
            lastsquare.Add(FirstRow);
            cycle += 1;
            newSudoku.Add(lastsquare);
        }

        mat = new int[syx, syx];
        sudoku = new List<int>[syx, syx];
        int cx = 0;
        int cy = 0;
        for (int c = 0; c < syx; c++)
        {
            for (int y = 0; y < sy; y++)
            {
                for (int x = 0; x < sx; x++)
                {
                    sudoku[y + cy, x + cx] = new List<int>();
                    sudoku[y + cy, x + cx].Add(newSudoku[c][y][x]);
                }
            }
            cx += sx;
            if (cx >= syx)
            {
                cy += sy;
                cx = 0;
            }
        }
    }

    bool validate(int y, int x, int n)
    {
        for (int num = 0; num < syx; num++)
        {
            if (n == sudoku[y, num][0])
                return false;
            if (n == sudoku[num, x][0])
                return false;
        }

        int y0 = (y / sy) * sy;
        int x0 = (x / sx) * sx;
        for (int i = 0; i < sy; i++)
        {
            for (int j = 0; j < sx; j++)
            {
                if (n == sudoku[y0 + i, x0 + j][0])
                    return false;
            }
        }
        return true;
    }

    public int marker()
    {
        if (morethantwo)
            return 0;
        int solvable = 0;

        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                if (sudoku[y, x][0] == 0 && sudoku[y, x].Count == 1)
                {
                    for (int n = 1; n < syx + 1; n++)
                    {
                        if (validate(y, x, n))
                        {
                            sudoku[y, x].Add(n);
                        }
                    }
                    solvable += marker();
                    sudoku[y, x] = new List<int>();
                    sudoku[y, x].Add(0);
                    return solvable;
                }
            }
        }
        return singles();
    }

    int singles()
    {
        if (morethantwo)
            return 0;
        int solvable = 0;

        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                if (sudoku[y, x][0] == 0)
                {
                    if (sudoku[y, x].Count < 2)
                    {
                        return solvable;
                    }
                    if (sudoku[y, x].Count == 2)
                    {
                        sudoku[y, x].RemoveAt(0);
                        List<int[]> removed = cleanup();
                        solvable += singles();
                        undo(removed);
                        int temp = sudoku[y, x][0];
                        sudoku[y, x][0] = 0;
                        sudoku[y, x].Add(temp);
                        return solvable;
                    }
                }
            }
        }
        return doubles(0);
    }

    int doubles(int y0)
    {
        if (morethantwo)
            return 0;
        int solvable = 0;

        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                if (sudoku[y, x][0] == 0 && sudoku[y, x].Count < sx)
                {
                    int last = sudoku[y, x][0];
                    sudoku[y, x].RemoveAt(0);
                    sudoku[y, x].Add(last);
                    List<int[]> removed = cleanup();

                    while (sudoku[y, x][0] != 0)
                    {
                        solvable += singles();
                        undo(removed);
                        last = sudoku[y, x][0];
                        sudoku[y, x].RemoveAt(0);
                        sudoku[y, x].Add(last);
                        removed = cleanup();
                    }
                    return solvable;
                }
            }
        }
        return solve(0);
    }

    int solve(int y0)
    {
        if (morethantwo)
            return 0;
        int solvable = 0;

        for (int y = y0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                if (sudoku[y, x][0] == 0)
                {
                    int last = sudoku[y, x][0];
                    sudoku[y, x].RemoveAt(0);
                    sudoku[y, x].Add(last);
                    List<int[]> removed = cleanup();

                    while (sudoku[y, x][0] != 0)
                    {
                        solvable += singles();
                        undo(removed);
                        last = sudoku[y, x][0];
                        sudoku[y, x].RemoveAt(0);
                        sudoku[y, x].Add(last);
                        removed = cleanup();
                    }
                    return solvable;
                }
            }
        }

        if (solvable == 0)
        {
            saveSudoku();
        }
        else if (solvable > 1)
        {
            morethantwo = true;
        }
        return solvable + 1;
    }

    List<int[]> cleanup()
    {
        List<int[]> removed = new List<int[]>();
        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                if (sudoku[y, x][0] == 0)
                {
                    foreach (int n in sudoku[y, x])
                    {
                        if (n != 0 && !validate(y, x, n))
                        {
                            removed.Add(new int[] { y, x, n });
                        }
                    }
                }
            }
        }
        foreach (int[] z in removed)
        {
            sudoku[z[0], z[1]].Remove(z[2]);
        }
        return removed;
    }

    void undo(List<int[]> removed)
    {
        foreach (int[] z in removed)
        {
            sudoku[z[0], z[1]].Add(z[2]);
        }
    }

    public void randomize()
    {
        numbers();
        rows();
        cols();
        rows2();
        cols2();
    }


    void numbers()
    {
        for (int n = 1; n < syx; n++)
        {
            int rn = rand.Next(1, syx);
            for (int y = 0; y < syx; y++)
            {
                for (int x = 0; x < syx; x++)
                {
                    if (sudoku[y, x][0] == n)
                        sudoku[y, x][0] = rn;
                    else if (sudoku[y, x][0] == rn)
                        sudoku[y, x][0] = n;
                }
            }
        }
    }

    void swapRows(int n1, int n2)
    {
        for (int i = 0; i < syx; i++)
        {
            int row = sudoku[n1, i][0];
            sudoku[n1, i][0] = sudoku[n2, i][0];
            sudoku[n2, i][0] = row;
        }
    }

    void swapCols(int n1, int n2)
    {
        for (int i = 0; i < syx; i++)
        {
            int row = sudoku[i, n1][0];
            sudoku[i, n1][0] = sudoku[i, n2][0];
            sudoku[i, n2][0] = row;
        }
    }

    void rows()
    {
        for (int n = 0; n < syx; n++)
        {
            int rn = rand.Next(0, sy - 1);
            int y0 = (n / sy) * sy;
            swapRows(n, rn + y0);
        }
    }


    void cols()
    {
        for (int n = 0; n < syx; n++)
        {
            int rn = rand.Next(0, sx - 1);
            int x0 = (n / sx) * sx;
            swapCols(n, rn + x0);
        }
    }


    void rows2()
    {
        for (int n = 0; n < sy; n++)
        {
            int rn = rand.Next(0, sy - 1);
            for (int i = 0; i < sy; i++)
            {
                swapRows(n * sy + i, rn * sy + i);
            }
        }
    }

    void cols2()
    {
        for (int n = 0; n < sx; n++)
        {
            int rn = rand.Next(0, sx - 1);
            for (int i = 0; i < sx; i++)
            {
                if (n * sx + i < syx && rn * sx + i < syx)
                    swapCols(n * sx + i, rn * sx + i);
            }
        }
    }

    public void removeNumbers()
    {
        int[] items = Enumerable.Range(0, syx * syx).ToArray();
        for (int i = 0; i < items.Length - 1; i++)
        {
            int j = rand.Next(i, items.Length);
            int temp = items[i];
            items[i] = items[j];
            items[j] = temp;
        }

        var watch = System.Diagnostics.Stopwatch.StartNew();
        long time = 0;
        int limit = (sy + sx) * 1000;
        foreach (int m in items)
        {
            int n = sudoku[m / syx, m % syx][0];
            if (n != 0)
            {
                time = watch.ElapsedMilliseconds;
                sudoku[m / syx, m % syx][0] = 0;
                if (marker() != 1)
                    sudoku[m / syx, m % syx][0] = n;
                if (watch.ElapsedMilliseconds - time > limit) break;
                morethantwo = false;
            }
        }
        watch.Stop();
    }

    public void matrixToSudoku()
    {
        sudoku = new List<int>[syx, syx];
        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                sudoku[y, x] = new List<int>();
                sudoku[y, x].Add(mat[y, x]);
            }
        }
    }

    public void saveSudoku()
    {
        mat = new int[syx, syx];
        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                mat[y, x] = sudoku[y, x][0];
            }
        }
    }

    public void printSudoku()
    {
        int log = syx.ToString().Length;
        string s = sx + "\n";
        string t = "";
        for (int i = 0; i < syx; i++)
        {
            for (int j = 0; j < syx; j++)
            {
                t = sudoku[i, j][0].ToString();
                if (t.Equals("0"))
                {
                    t = "-";
                    while (t.Length < log)
                        t += "-";
                }
                while (t.Length < log)
                    t = "0" + t;
                s += t;
            }
            s += "\n";
        }
        //Console.Write(s);
        File.WriteAllText("output.txt", s);
    }

    public bool validateSudoku()
    {
        for (int y = 0; y < syx; y++)
        {
            for (int x = 0; x < syx; x++)
            {
                int n = sudoku[y, x][0];
                sudoku[y, x][0] = 0;
                if (n != 0 && !validate(y, x, n))
                {
                    Console.WriteLine("Incorrect :(");
                    sudoku[y, x][0] = n;
                    return false;
                }
                sudoku[y, x][0] = n;
            }
        }
        Console.WriteLine("Correct!");
        return true;
    }
}