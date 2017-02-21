__author__ = 'Gaurav'


def number_of_0s_in_fact(n):
    if not n:
        return None
    else:
        i = 5
        count = 0
        while (n/i > 0):
            count += n/i
            i *= 5
    return count

def find_max(a, b):
    z = a -b
    i = (z >> 31) & 0x1
    max = a - i * z
    min = b + i*z
    return max, min


def main():
    num = number_of_0s_in_fact(26)
    print num
    max_n, min_n = find_max(3, 5)
    print max_n, min_n
if __name__ == '__main__':
    main()