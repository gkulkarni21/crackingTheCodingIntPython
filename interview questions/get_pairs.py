__author__ = 'Gaurav'


def get_pairs(array, sum):
    pairs = {}
    list_of_pairs = []
    for x in array:
        if sum - x in pairs:
            pair = []
            pair.append(x)
            pair.append(sum-x)
            list_of_pairs.append(pair)
        pairs[x] = sum-x
    return list_of_pairs

def main():
    array = [-2, -1, 0, 3, 4, 6, 7]
    lists = get_pairs(array, 4)
    print "".join(lists)

if __name__ == '__main__':
    main()