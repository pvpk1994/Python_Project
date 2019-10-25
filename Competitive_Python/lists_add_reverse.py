'''
Sum-Linked Lists - Medium
Source:: Leet Code
Author: Pavan Kumar Paluri
'''
'''
Add two single linked lists and reverse the digits
and add them, then decode the result and put it 
back into a new linked list
'''
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
            print(f'Data read: {temp.data}')
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


def add_lists(list_head1: Node, list_head2: Node) -> SingleList:
    list_num1 = []
    list_num2 = []
    if list_head1 is None:
        list_num1.append(0)
    if list_head2 is None:
        list_num2.append(0)
    while list_head1 is not None:
        list_num1.append(list_head1.data)
        list_head1 = list_head1.next
    while list_head2 is not None:
        list_num2.append(list_head2.data)
        list_head2 = list_head2.next

    print(f'List_1: {list_num1}')
    print(f'List_2: {list_num2}')
    list_num2.reverse()
    list_num1.reverse()
    print(f'List_1: {list_num1}')
    print(f'List_2: {list_num2}')
    res1 = merge_list_elements(list_num1)
    res2 = merge_list_elements(list_num2)
    new_res = res1 + res2
    print(new_res)
    new_head = split_list_elements(new_res)
    return new_head


def merge_list_elements(list_num: list) -> int:
    if list_num is None:
        return 0
    result = int("".join(map(str, list_num)))
    return result


def split_list_elements(num: int) -> SingleList:
    new_head = SingleList()
    list_new = list(str(num))
    list_4 = []
    for val in list_new:
        list_4.append(int(val))
    list_4.reverse()
    print(list_4)
    for val in list_4:
        new_head.append(val)
    return new_head


# main section..
llist = SingleList()
llist.append(3)
llist.append(4)
llist.append(5)
llist.print_list()
print(f'\n')
llist_new = SingleList()
llist_new.append(5)
llist_new.append(7)
llist_new.append(9)

llist_new.print_list()
print(f'\n')
# Returns a head
ll_new = add_lists(llist.head, llist_new.head)
ll_new.print_list()


