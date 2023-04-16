def find_insert_position(array, number):
    left = 0
    right = len(array) - 1

    if(len(array) == 0):
        return 0

    while left <= right:
        middle = (left+right) // 2
        if array[middle] == number:
            return middle
        elif array[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return left

if (__name__ == '__main__'):
    A = [1,2,4,5]
    x = 6
    print(find_insert_position(A, x))