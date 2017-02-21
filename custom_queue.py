__author__ = 'Gaurav'

class Node:

    def __init__(self, content):
        self.content = content
        self.next = None

class Custom_Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def Enqueue(self, node):
        self.size += 1
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = self.head
            return
        self.tail.next = node
        self.tail = node

    def Dequeue(self):
        if self.size == 0:
            return ValueError("Queue is empty")
        next_node = self.head.next
        self.head = next_node
        self.size -= 1


    def front(self):
        return self.head

    def isEmpty(self):
        if self.size == 0:
            return True
        else: return False

    def print_elements(self):
        current = self.head
        while current is not None:
            print current.content,
            current = current.next

def main():
    queue = Custom_Queue()
    node_one = Node(2)
    node_two = Node(3)
    node_three = Node(4)
    queue.Enqueue(node_one)
    # queue.print_elements()
    queue.Enqueue(node_two)
    queue.print_elements()
    queue.Dequeue()
    queue.print_elements()
if __name__ == '__main__':
    main()