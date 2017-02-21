from Queue import Queue

__author__ = 'Gaurav'

class BSTNode:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None

def insert(root, node):
    if root == None:
        root = node
    else:
        if root.content > node.content:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

def delete(root, node):
    if root is None:
        return
    elif root.content < node.content:
        root.right = delete(root.right, node)
    elif root.content > node.content:
        root.left = delete(root.left, node)

    # Now we have found the node to be deleted
    elif root.left is None and root.right is None:
        del root
        return root
    elif root.left is None:
        root = root.right
        del root.right
        return root
    elif root.right is None:
        root = root.left
        del root.left
        return root
    elif root.left is not None and root.right is not None:
        root = min_node(root.right)
        root.right = delete(root.right, node)
        return root

def min_node(root):
    if root is None:
        return
    min = root
    if root.left is not None:
        min = min_node(root.left)
    return min



def search(root, node):
    if root ==  node:
        return root
    else:
        if root.content < node.content:
            if root.right == node:
                return root.right
            else:
                search(root.right, node)
        if root.content > node.content:
            if root.left == node:
                return root.left
            else:
                search(root.left, node)

def breadth_first(root):
    queue = Queue()
    queue.put(root)
    while queue:
        node = queue.get()
        print node.content
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
    return

def breadth_first_level_wise(root):
    this_level = [root]
    while this_level:
        new_level = []
        for n in this_level:
            print n.content,
            if n.left:
                new_level.append(n.left)
            if n.right:
                new_level.append(n.right)
        print
        this_level = new_level

def preOrder(root):
    if not root:
        return
    print root.content
    preOrder(root.left)
    preOrder(root.right)

def InOrder(root):
    if not root:
        return
    InOrder(root.left)
    print root.content
    InOrder(root.right)

def PostOrder(root):
    if not root:
       return
    PostOrder(root.left)
    PostOrder(root.right)
    print root.content

def main():
    node_one = BSTNode(2)
    node_two = BSTNode(3)
    node_three = BSTNode(7)
    node_four = BSTNode(8)
    node_five = BSTNode(1)
    node_six = BSTNode(11)
    node_seven = BSTNode(6)
    root = BSTNode(5)
    insert(root, node_one)
    insert(root, node_two)
    insert(root, node_three)
    insert(root, node_four)
    insert(root, node_five)
    insert(root, node_six)
    insert(root, node_seven)
    print "PreOrder:"
    preOrder(root)
    print "InOrder:"
    InOrder(root)
    print "PostOrder:"
    PostOrder(root)
    # value =  search(root, node_seven).content
    # print "found"
    min = min_node(root)
    print min.content
    # deleted_node = delete(root, node_four)
    # print "After deleting:"
    # preOrder(root)
    # print "BFS:"
   # breadth_first(root)
    print "Level_wise:"
    breadth_first_level_wise(root)
if __name__ == '__main__':
    main()