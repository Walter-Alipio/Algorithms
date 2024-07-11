def binary_search(list, item):
    min = 0
    max = len(list) - 1

    while min <= max:
        center = (min + max) // 2
        guess = list[center]
        if guess == item:
            return center
        if guess > item:
            max = center - 1
        else:
            min = center + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) #1
print(binary_search(my_list, -1)) #None