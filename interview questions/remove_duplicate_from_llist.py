__author__ = 'Gaurav'

from LinkedList import CustomLinkedList, Node

def remove_duplicates_from_linkedL(linkedlist):
    hash_map = {}
    current = linkedlist.head
    while current is not None:
        if current.content not in hash_map:
            hash_map[current.content] = 1
        else:
            linkedlist.delete(current)
        current = current.next

    return linkedlist

def delete_without_using_HT(linkedlist):
    current = linkedlist.head
    while current is not None:
        iterator = current.next
        while iterator is not None:
            if iterator.content == current.content:
                linkedlist.delete(iterator)
            iterator = iterator.next
        current = current.next
    return linkedlist

def find_nth_to_the_last(linked_list, n):
    start = linked_list.head
    end = linked_list.head
    for x in range(0,n):
        end = end.next
    while start is not None and end is not None:
        start = start.next
        end = end.next
    return start

def find_nth_with_my_list(linked_list, n):
    if n >= linked_list.size:
        return ValueError("n does not exists")
    position = linked_list.size - n
    current = linked_list.head
    for x in range(0,position):
        current = current.next
    return current

def add_numbers_using_linked_list(node1, node2, carry):
    if node1 is None and node2 is None:
        return
    result = Node(carry)
    value = carry
    value = value + node1.content + node2.content
    result.content = value % 10
    nextNode = add_numbers_using_linked_list(None if node1 is None else node1.next,
                                             None if node2 is None else node2.next,
                                             1 if value > 10 else 1
    )
    result.next = nextNode
    return result

def main():
    custom_linked_list = CustomLinkedList()
    node1 = Node(5)
    node2 = Node(7)
    node3 = Node(7)
    node4 = Node(8)
    node5 = Node(9)
    custom_linked_list.insert_at_the_beginning(node1)
    custom_linked_list.insert_at_the_beginning(node2)
    custom_linked_list.insert_at_the_beginning(node3)
    custom_linked_list.insert_at_the_beginning(node4)
    custom_linked_list.insert_at_the_beginning(Node(5))
    custom_linked_list.print_list(custom_linked_list.head)
    print "\n"
    # linked_list = remove_duplicates_from_linkedL(custom_linked_list)
    # linked_list.print_list(linked_list.head)
    # linked_list_two = delete_without_using_HT(custom_linked_list)
    # linked_list_two.print_list(linked_list_two.head)
    # x = find_nth_to_the_last(custom_linked_list, 2)
    # print x.content
    # y = find_nth_with_my_list(custom_linked_list, 2)
    # print y.content
    one = Node(4)
    two = Node(3)
    list_one = CustomLinkedList()
    list_one.insert_at_the_beginning(one)
    list_one.insert_at_the_beginning(two)
    list_two = CustomLinkedList()
    list_two.insert_at_the_beginning(two)
    list_two.insert_at_the_beginning(one)
    three = add_numbers_using_linked_list(list_one.head, list_two.head, 0)


if __name__ == '__main__':
    main()