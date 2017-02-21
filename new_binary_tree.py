__author__ = 'Gaurav'

class BSTnode:
    def __init__(self, content):
        self.data = content
        self.l_child = None
        self.r_child = None

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def main():
    r = BSTnode(3)
    binary_insert(r, BSTnode(7))
    binary_insert(r, BSTnode(1))
    binary_insert(r, BSTnode(5))

    print "in order:"
    in_order_print(r)

    print "pre order"
    pre_order_print(r)

if __name__ == '__main__':
    main()