__author__ = 'Gaurav'

def find_rotation(array, number):
    length = len(array)
    high = length - 1
    low = 0
    while low <= high:
        mid = (high + low)/2
        next = (mid + 1) % length
        prev = (mid + length - 1) % length
        if array[mid] <= array[next] and array[mid] <= array[prev]:
            break
        elif array[mid] <= array[high]:
            high = mid - 1
        else:
            low = mid + 1

    if number == array[mid]:
        return mid
    if number < array[mid]:
        index = binary_search(array, mid + 1, high, number)
    else:
        index = binary_search(array, 0, mid - 1, number)

    return index


def binary_search(array, low, high, value):
    while low <= high:
        mid = (low + high)/2
        if array[mid] == value:
            return mid
        else:
            if value < array[mid]:
                high = mid - 1
            else:
                low = mid + 1


def main():
    arr = [3, 5, 8, 9, 1, 2]
    ind = find_rotation(arr, 5)
    print ind

if __name__ == '__main__':
    main()