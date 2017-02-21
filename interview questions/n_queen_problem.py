__author__ = 'Gaurav'

BOARD_SIZE = 8

def solve(n):
    if n ==0:
        return [[]]
    solutions = []
    small_solution = solve(n-1)
    for solution in small_solution:
        for column in range(1,BOARD_SIZE + 1 ):
            if not under_attack(column, solution):
                print "Solution:"
                print solution
                solutions.append(solution + [(n, column)])
    return solutions

def under_attack(column, existing_queens):
    row = len(existing_queens)+ 1
    for queen in existing_queens:
        r,c = queen
        if r == row: # check row
            return True
        if c == column: #check column
            return True
        if (column - c) == (row - r): # check left diagonal
            return True
        if (column - c) == -(row - r): #check right diagonal
            return True
    return False

def main():
    answers = solve(8)
    for answer in answers:
        print answer

if __name__ == '__main__':
    main()