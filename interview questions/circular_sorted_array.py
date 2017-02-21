__author__ = 'Gaurav'


def find_rotation(array):
    length = len(array)
    high = length - 1
    low = 0
    while low <= high:
        if array[low] < array[high]:
            return low
        else:
            mid = (low + high)/2
            next = (mid + 1) % length
            prev = (mid + length - 1) % length
            if array[mid] <= array[next] and array[mid] >= array[prev]:
                return mid
            elif array[mid] <= array[high]:
                high = mid - 1
            else:
                low = mid + 1


def binary_search(array, value):
    length = len(array)
    low = 0
    high = length - 1
    while low <= high:
        mid = (low + high)/2
        if array[mid] == value:
            return value
        else:
            if value < array[mid]:
                high = mid - 1
            else:
                low = mid + 1

def first_occurence(array, n):
    length = len(array)
    result = -1
    low = 0
    high = length - 1
    while low <= high:
        mid = (low + high)/2
        if array[mid] == n:
            result = mid
            high = mid - 1
        else:
            if n < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return result

def last_occurence(array, n):
    length = len(array)
    low = 0
    result = -1
    high = length - 1
    while low <= high:
        mid = (low + high)/2
        if array[mid] == n:
            result = mid
            low = mid + 1
        else:
            if n < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return result

def number_of_occur(array, n):
    smaller = first_occurence(array, n)
    higher = last_occurence(array, n)
    count = higher - smaller + 1
    return count


def main():
    array = [12, 15, 18, 3, 7, 9]
    n = find_rotation(array)
    print n
    array_two = [2, 3, 4, 5, 5, 5, 5, 5, 6, 9]
    print "First occurence of 5:  %d" % first_occurence(array_two, 5)
    print "Last occurence of 5: %d" % last_occurence(array_two, 5)
    print "count: %d"  % number_of_occur(array_two, 5)

if __name__ == '__main__':
    main()