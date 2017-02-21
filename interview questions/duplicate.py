__author__ = 'Gaurav'

def remove_duplicate(input_str):
    if len(input_str) == 0:
        return
    new_string = []
    for char in input_str:
        if char not in new_string:
            new_string.append(char)
    return (''.join(new_string))

def main():
    new_string = remove_duplicate("aabb")
    print new_string
    new_string = remove_duplicate("abcd")
    print new_string
    new_string = remove_duplicate("")
    print new_string
    new_string = remove_duplicate("abababab")
    print new_string

if __name__ == '__main__':
    main()