from Queue import Queue
__author__ = 'Gaurav'


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

def dfs(graph, start):
    stack = []
    stack.append(start)
    visited = set()
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.add(node)
            for adj in graph.get(node, []):
                stack.append(adj)
    return visited

def bfs(graph, start, end):
    queue = []
    visited = []
    queue.append([start])
    while queue:
        path = queue.pop()
        node = path[-1]
        if node == end:
            return path
        elif node not in visited:
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited.append(node)
    return queue

def main():
    graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }
    # print dfs(graph, '1')
    print bfs(graph, '2', '12')
    visited  = dfs(graph, '1')
if __name__ == '__main__':
    main()