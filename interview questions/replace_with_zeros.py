__author__ = 'Gaurav'


def replace_with_zeros(matrix):
    row = [0 for x in range(len(matrix))] #cannot directly set value at particular index to 1 without initializing it
    column = [0 for x in range(len(matrix[0]))]
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            if matrix[x][y] == 0:
                row[x]= 1
                column[y] = 1
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            if row[x] == 1 or column[y] == 1:
                matrix[x][y] = 0

    return matrix

def print_matrix(matrix):
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            print matrix[x][y],

def main():
    matrix = [[0 for x in range(4)]for x in range(4)]
    matrix[0][0] = 1
    matrix[0][1] = 2
    matrix[0][2] = 1
    matrix[0][3] = 1
    matrix[1][0] = 0
    matrix[1][1] = 1
    matrix[1][2] = 1
    matrix[1][3] = 1
    matrix[2][0] = 1
    matrix[2][1] = 1
    matrix[2][2] = 1
    matrix[2][3] = 1
    matrix[3][0] = 1
    matrix[3][1] = 1
    matrix[3][2] = 1
    matrix[3][3] = 0
    new_matrix = replace_with_zeros(matrix)

if __name__ == '__main__':
    main()

