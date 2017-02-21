__author__ = 'Gaurav'

from LinkedList import CustomLinkedList, Node

def if_circular(linked_list):
    slower = linked_list.head
    faster = linked_list.head
    while slower.next is not None and faster.next is not None:
        slower = slower.next
        faster = faster.next.next
        if slower == faster:
            return True
    return False

def find_start_of_loop(linked_list):
    """
    Works same as that of if_circular. However, when slower and faster are same, it is called as "meeting point".
    By keeping faster at meeting point, we reiterate slower from begining. Once they meet again, it is the start
    of loop
    :param linked_list:
    :return: node starting loop
    """
    slower = linked_list.head
    faster = linked_list.head
    while faster.next is not None:
        slower = slower.next
        faster = faster.next.next
        if slower == faster:
            break
    slower = linked_list.head
    while (slower != faster):
        slower = slower.next
        faster = faster.next
    return faster

def main():
    one = Node(2)
    two = Node(3)
    three = Node(4)
    one.next = two
    list_one = CustomLinkedList()
    list_one.insert_at_the_beginning(one)
    list_one.insert_at_the_beginning(two)
    list_one.insert_at_the_beginning(three)
    four = find_start_of_loop(list_one)

if __name__ == '__main__':
    main()
