#include <iostream>
#include <stdexcept>

int binarySearch(int *list, int item)
{
    int min = 0;
    int max = sizeof(list) - 1;
    while (min <= max)
    {
        int center = (min - max) / 2;
        int guess = list[center];
        if (guess == item)
        {
            return center;
        }
        if (guess > item)
        {
            max = center - 1;
        }else
        {
            min = center + 1;
        }     
    }
    throw std::runtime_error("Element no found");
}
 
 int main()
 {
    int myList[] = { 1,3,5,7,9 };

    std::cout << binarySearch(myList, 3) << std::endl;
    std::cout << binarySearch(myList, -1) << std::endl;
 }