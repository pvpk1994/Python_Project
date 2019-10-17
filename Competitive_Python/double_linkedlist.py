'''
Operations on Double Linked List ~ Pavan Kumar Paluri
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self):
        self.head = None

    '''
    Push 
    '''
    def push(self, new_data):
        new_node = Node(new_data)
        # Link the new node to the head...
        new_node.next = self.head
        new_node.prev = None

        # What if self.head is not none..
        if self.head is not None:
            self.head.prev = new_node
        # Now switch the head to point to new_node
        self.head = new_node

    '''
    Append
    '''
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        # if self.head is Null ??
        if self.head is None:
            self.head = new_node
            self.head.prev = None

        # If self.head is not null,
        # iterate through the list until last node...
        elif self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            # when control is here, implies current_node.next is none
            current_node.next = new_node
            new_node.prev = current_node

    '''
    insert After a given node..
    '''
    def insert_after(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print(f'Insertion of new node after a given \n'
                  f'is not possible')
        # assign prev_node's next to the new_node's next..
        new_node.next = prev_node.next
        # Assign prev_node's next to new_node
        prev_node.next = new_node

        new_node.prev = prev_node

        # if new_node's next is not empty, then...
        if new_node.next is not None:
            new_node.next.prev = new_node

    def print_list(self):
        temp = self.head
        counter = 0
        '''
        Traversal in forward direction...
        '''
        while temp is not None:
            counter += 1
            print(f'Data read: {float(temp.data)}')
            node_itr = temp
            temp = temp.next
        '''
        Traversal in reverse direction...
        '''
        print(f'\n Data read in reverse direction...\n')
        while node_itr is not None:
            print(f'Data read: {float(node_itr.data)}')
            node_itr = node_itr.prev
        print(f'\n')
        return counter


'''
Main()
'''
if __name__ == '__main__':
    llist = DoubleLL()
    llist.push(23)
    llist.push(35)
    llist.push(12)
    llist.push(99)
    llist.print_list()

    # Append mode...
    llist_app = DoubleLL()
    llist_app.append(3)
    llist_app.append(4)
    llist_app.append(5)
    llist_app.insert_after(llist_app.head, 13)
    llist_app.append(56)
    llist_app.print_list()









