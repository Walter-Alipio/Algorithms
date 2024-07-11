static int? BinarySearch(int[] list, int item)
{
    int min = 0 ;
    int max = list.Length - 1;
    while (min <= max)
    {
        int center = (min + max) / 2 ;
        int guess = list[center];
        if (guess == item)
            return center;
        if (guess > item)
            max = center - 1;
        else
        {
            min = center + 1;
        }
    }
    return null;
}

int[] my_list = [1, 3, 5, 7, 9];

System.Console.WriteLine(BinarySearch(my_list, 3));
System.Console.WriteLine(BinarySearch(my_list, -1) is null);