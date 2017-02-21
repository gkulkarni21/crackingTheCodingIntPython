__author__ = 'Gaurav'


def merging(array1, array2):
    '''
    Used to merge two arrays in sorted way such that array1 has large buffer at the end and can accomodate array2
    :param array1:
    :param array2:
    :return:
    '''
    len_arr1 = len(array1)
    len_arr2 = len(array2)
    i=j=k=0
    new_array = [0 for x in range(len_arr1 + len_arr2)]
    while (i<len_arr1 and j<len_arr2):
        if  array1[i] < array2[j]:
            new_array[k] = array1[i]
            i += 1
        else:
            new_array[k] = array2[j]
            j += 1
        k += 1

    while i < len_arr1:
        new_array[k] = array1[i]
        i += 1
        k += 1

    return new_array

def main():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6]
    out = merging(arr1, arr2)
    print out

if __name__ == '__main__':
    main()
