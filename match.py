__author__ = 'Gaurav'

def match(pattern, filenames):
    for name in filenames:
        for char in




def main():
    print ["abcd", "dabc", "abc"] == match("?abc*", ["abcd", "dabc", "abc", "efabc", "eadd"])
    print ["abcd", "dabc", "abc"] == match("?a**c*", ["abcd", "dabc", "abc", "efabc", "eadd"])

if __name__ == '__main__':
    main()