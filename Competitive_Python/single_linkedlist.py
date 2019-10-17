'''
All operations on Single Linked list
Author: Pavan Kumar Paluri
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insertafter(self, prev_node, new_data):
        if prev_node is None:
            '''
            Insertion not possible
            '''
            print(f'The given node is empty, \n'
                  f'Insertion not possible...')
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        # if head is not null...
        last = self.head
        while last.next:
            last = last.next
        # if here, implies we have come out of loop...
        last.next = new_node

    '''
    Remove nth node from a given Linked lIst...
    '''
    def n_remove(self, position):
        current = self.head
        for i in range(0, position-1):
            current = current.next
        # now current points to the node before the node that has to be deleted...
        new_node = current.next.next
        # Now de-link current.next
        del current.next
        current.next = new_node

    '''
    Remove the nth node from the end...
    '''
    def n_remove_last(self, positions):
        current = self.head
        positions = (self.print_list()-1)-positions
        print(f'new_position:{positions}')
        # if position is 0, remove current and shift head to next..
        if positions == 0:
            self.head = current.next
            del current
            return
        for i in range(0, positions-1):
            current = current.next
        new_node = current.next.next
        del current.next
        current.next = new_node

    '''
    Given nth position, return 
    square root of the value in that node...
    '''
    def sqrt_n(self, position):
        current = self.head
        for i in range(0,position-1):
            current = current.next
        # if here, our current.next now points to the nth node
        current.next.data = pow(current.next.data, 0.5)

    def print_list(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            print(f'Data read: {float(temp.data)}')
            temp = temp.next
        return counter

    '''
    given data, find the occurance of that data in multiple nodes across
    the list...
    '''
    def num_occurrence(self, data):
        temp = self.head
        counter_times = 0
        while temp:
            if temp.data is data:
                counter_times += 1
            temp = temp.next
        return counter_times


# main section..
llist = SingleList()
llist.push(33)
llist.push(45)
llist.append(36)
llist.append(33)
llist.append(36)
llist.append(45)
llist.append(36)
llist.append(36)
llist.print_list()
print(f'36 has occurred {llist.num_occurrence(36)} times')

print(f'\n')
llist.n_remove_last(2)
#llist.sqrt_n(1)
length_list = llist.print_list()
print(f'Length of the linked list: {length_list}')

