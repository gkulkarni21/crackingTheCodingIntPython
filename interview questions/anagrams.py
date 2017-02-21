__author__ = 'Gaurav'

def ifAnagrams(str1, str2):
    unique_chars = {}
    unique_chars_str2 = {}
    count = 1
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char not in unique_chars:
            unique_chars[char] = count
        else:
            unique_chars[char] = unique_chars[char] + 1
        if char in str2:
            unique_chars[char] = unique_chars[char] + 1

    for ch in unique_chars:
        if unique_chars[ch]%2 != 0:
            return False
    return True

def ifAnagram_sort(str_input1, str_input2):
    str_input1 = sorted(str_input1)
    str_input2 = sorted(str_input2)
    if str_input1 == str_input2:
        return  True
    else:
        return  False

def replace_space(str1):
    str_new = ''
    for char in str1:
        if char != ' ':
            str_new = str_new + char
        else:
            str_new = str_new + "%20"
    return str_new

def isSubstring(str1, str2):
    if str1 in str2:
        return True
    else:
        return False

def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return False
    str1_concat = str1 + str1
    if isSubstring(str2, str1_concat):
        return True
    else:
        return False


def main():
    print ifAnagrams("abcd", "dcab")
    print ifAnagram_sort("abcd","dccb")
    print replace_space("This is")
    print isRotation("BAB","ABB")

if __name__ == "__main__":
    main()