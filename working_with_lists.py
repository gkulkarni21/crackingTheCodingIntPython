__author__ = 'Gaurav'


def drop_ship_dropship(x):
    if x % 15 == 0:
        print 'dropship'
    elif x % 3 == 0:
        print 'drop'
    elif x % 5 == 0:
        print 'ship'
    else: print x

def flatten(input):
    return [x for num in input for x in num]

def main():
    filter(drop_ship_dropship, range(2, 25))
    list_op = flatten([[1,2,4], [5], [3, 5, 1]])
    print list_op
if __name__ == '__main__':
    main()