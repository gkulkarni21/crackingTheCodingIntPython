__author__ = 'Gaurav'

from Stack import Stack
from LinkedList import Node

class custom_queue_stack(object):
    """
    To implement queue using two stacks, we perform push operation on one stack. Perform peek and dequeue on other stack
    While performing dequeue and peek, move all contents from stack one to stack two if stack two is empty.
    """

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def peek(self):
        if not self.stack2.isEmpty():
            return self.stack2.top()
        while not self.stack1.isEmpty():
            value = self.stack1.pop()
            self.stack2.push(value)
        return self.stack2.top()

    def dequeue(self):
        if not self.stack2.isEmpty():
            return self.stack2.pop()
        while not self.stack1.isEmpty():
            value = self.stack1.pop()
            self.stack2.push(value)
        return self.stack2.pop()


def main():
    new_queue = custom_queue_stack()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    new_queue.enqueue(one)
    new_queue.enqueue(two)
    print new_queue.peek().content

if __name__ == '__main__':
    main()