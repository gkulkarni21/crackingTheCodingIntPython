__author__ = 'Gaurav'


class Node:
    def __init__(self, content):
        self.content = content
        self.next = None


class CustomLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def reverse_recursive(self, node):
        while node.next is None:
            self.head = node
            return
        self.reverse_recursive(node.next)
        temp = node.next
        temp.next = node
        node.next = None

    def insert_at_the_beginning(self, node):
        self.size += 1
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def delete(self, node):
        previous = self.head
        if self.head == node:
            nextNode = self.head.next
            self.head = nextNode
            return
        current = self.head.next
        while current is not None:
            if current == node:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next


    def print_list(self, node):
        while node is not None:
            print node.content,
            node = node.next

def main():
    custom_linked_list = CustomLinkedList()
    node1 = Node(5)
    node2 = Node(7)
    node3 = Node(6)
    node4 = Node(8)
    node5 = Node(9)
    custom_linked_list.insert_at_the_beginning(node1)
    custom_linked_list.insert_at_the_beginning(node2)
    custom_linked_list.insert_at_the_beginning(node3)
    custom_linked_list.insert_at_the_beginning(node4)
    custom_linked_list.print_list(custom_linked_list.head)
    # custom_linked_list.delete(node2)
    # custom_linked_list.print_list(custom_linked_list.head)
    print
    custom_linked_list.reverse_recursive(custom_linked_list.head)
    custom_linked_list.print_list(custom_linked_list.head)

if __name__ == '__main__':
    main()