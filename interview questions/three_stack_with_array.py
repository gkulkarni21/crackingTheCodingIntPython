__author__ = 'Gaurav'

class three_stack_array(object):
    def __init__(self, stack_size, number_of_stacks):
       self.stack_size = stack_size
       self.holding_array = [0 for x in range(self.stack_size*number_of_stacks)]
       self.top_pointers = [0 for x in range(number_of_stacks)]

    def push(self, stack_number, value):
        index = self.stack_size * stack_number + self.top_pointers[stack_number] + 1
        self.holding_array[index] = value
        self.top_pointers[stack_number] += 1

    def pop(self, stack_number):
        if self.top_pointers[stack_number] == 0:
            return ValueError("Stack is empty")
        index = self.stack_size * stack_number + self.top_pointers[stack_number]
        self.top_pointers[stack_number] -= 1
        value = self.holding_array[index]
        self.holding_array[index] = 0
        return value

    def peek(self, stack_number):
        index = self.stack_size * stack_number + self.top_pointers[stack_number]
        value = self.holding_array[index]
        return value

    def isEmpty(self, stack_number):
        if self.top_pointers[stack_number] == 0:
            return True

def main():
    stack = three_stack_array(200, 5)
    stack.push(0, 5)
    stack.push(1, 4)
    stack.push(2, 3)
    stack.push(3, 4)
    stack.push(0, 6)
    one = stack.peek(0)
    two = stack.peek(1)
    three = stack.peek(2)
    print one, two, three
    stack.pop(0)
    print "ha"


if __name__ == '__main__':
    main()