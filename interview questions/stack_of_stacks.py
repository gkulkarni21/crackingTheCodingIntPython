__author__ = 'Gaurav'


class stack_of_stacks(object):

    def __init__(self):
        self.stack_list = []
        self.capacity = 10
        self.stack_list_size = 0

    def get_last_stack(self):
        if self.stack_list_size == 0:
            return None
        return self.stack_list[self.stack_list_size - 1]

    def push(self, value):
        last_stack = self.get_last_stack()

        if (last_stack is None or last_stack.isAtCapactiy):
            next_stack = Stack(self.capacity)
            next_stack.push(value)
            self.stack_list.append(next_stack)
            self.stack_list_size += 1
        else:
            last_stack.push(value)


    def pop(self):
        last_stack = self.get_last_stack()
        if last_stack is not None:
            value = last_stack.pop()
            self.stack_list_size-= 1


class Node(object):
    def __init__(self, content):
        self.content = content
        self.next = None

class Stack(object):
    def __init__(self,capacity, head=None):
        self.head = head
        self.size = 0
        self.capacity = capacity

    def isAtCapactiy(self):
        if self.size == self.capacity:
            return True
        return False

    def push(self, node):
        if self.size == 0:
            self.head = node
            self.size += 1
            return
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        current = self.head
        nextNode = self.head.next
        self.head = nextNode
        self.size -= 1
        return current

def main():
    one = Node(2)
    stacks = stack_of_stacks()
    for x in range(0,12):
        stacks.push(one)
    print stacks.stack_list_size

if __name__ == '__main__':
    main()