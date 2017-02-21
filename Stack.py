import sys

__author__ = 'Gaurav'


class Node:
    def __init__(self, content):
        self.content = content
        self.next = None

class Stack(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def push(self, node):
        self.size += 1
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def pop(self):
        self.size -= 1
        nextnode = self.head.next
        self.head = nextnode
        return nextnode

    def top(self):
        return self.head

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

def reverse_a_string(input_str):
    stack = []
    for ch in input_str:
        stack.append(ch)
    for elem in stack:
        elem = stack.pop()
        out_str = ''

    return out_str

def if_balanced_paran(input_exp):
    opening = "({["
    closing = ")}]"
    stack = []
    for ch in input_exp:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def main():
    stack = Stack()
    node_one = Node(2)
    node_two = Node(3)
    node_three = Node(4)
    stack.push(node_one)
    stack.push(node_three)
    out = reverse_a_string("abcd")
    print out
    balanced = if_balanced_paran("{ 4 + )")
    print balanced
if __name__ == '__main__':
    main()