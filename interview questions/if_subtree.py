__author__ = 'Gaurav'

from binary_search_tree import BSTNode, insert

def isSubtree(Tree1, Tree2):
    """
    if Tree2 is subtree of Tree1
    :param Tree1:
    :param Tree2:
    :return: boolean
    """
    if Tree2 is None:
        return True
    if Tree1 is None:
        return False
    if ifIdentical(Tree1.head, Tree2.head):
        return True
    return (isSubtree(Tree1.left, Tree2)
    or isSubtree(Tree1.right, Tree2)
    )

def ifIdentical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return (node1.content== node2.content
    or ifIdentical(node1.left, node2.left)
    or ifIdentical(node1.right, node2.right)
    )

