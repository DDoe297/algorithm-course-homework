class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


def LinkedList():
    head = None


def reverse(node):
    if (node == None or node.next == None):
        return node
    r = reverse(node.next)
    node.next.next = node
    node.next = None
    return r


def printList():
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next


def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref


if __name__ == '__main__':
    head = LinkedList()
    head = push(head, 1)
    head = push(head, 2)
    head = push(head, 3)
    head = push(head, 4)

    print("Given linked list")
    printList()

    head = reverse(head)

    print("\nReversed Linked list")
    printList()
