'''
Merge two given linked lists at alternate positions
Author: Pavan Kumar Paluri
'''

counter = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LL:
    def __init__(self):
        self.head = None

    def push_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self, head_node):
        temp = head_node
        new_temp = None
        while temp is not None:
            print(f'{temp.data}')
            new_temp = temp
            temp = temp.next
        # Comes out, here, new_temp is at last node
        print('Reversal\n')
        while new_temp is not None:
            print(f'{new_temp.data}')
            new_temp = new_temp.prev


def merger(head1: Node, head2: Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    # Alternate LL1 with LL2 elements..
    return merge(head1, head2)


def merge(head_old, head_new):
    global counter
    if head_old is None:
        return head_new
    if head_new is None:
        return head_old
    counter += 1
    if counter % 2 == 0:
        head_old.next = merge(head_old.next, head_new)
        head_old.next.prev = head_old
        head_old.prev = None
        return head_old
    else:
        head_new.next = merge(head_old, head_new.next)
        head_new.next.prev = head_new
        head_new.prev = None
        return head_new


if __name__ == '__main__':
    # Linked List 1
    def_node = LL()
    def_node.push_node(4)
    def_node.push_node(5)
    def_node.push_node(8)
    # def_node.print_list()

    # Linked List 2
    def_node_new = LL()
    def_node_new.push_node(6)
    def_node_new.push_node(13)
    def_node_new.push_node(1)
    # def_node_new.print_list()

    head_new = merger(def_node.head, def_node_new.head)
    LL().print_list(head_new)
