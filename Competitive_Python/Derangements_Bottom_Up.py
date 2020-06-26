# Exploring the bottom up solution for the count derangements problem
# Author: Pavan Kumar Paluri


class derangment:
    def __init__(self, list_size):
        # init a list with -1's
        self.list_size = list_size
        self.list_num = [-1]*(list_size + 1)
        '''
        In bottom up approach, we work from bottom to top, hence evaluate all the elements as we tend towards right end
        '''
        for num in range(1, list_size+1):
            if num == 1:
                self.list_num[num] = 0
            elif num == 2:
                self.list_num[num] = 1
            else:
                self.list_num[num] = (num - 1) * (self.list_num[num - 1] + self.list_num[num-2])

    def bottom_up(self):
        return self.list_num[self.list_size]


if __name__ == '__main__':
    for i in range(1, 64):
        print(f'result for {i} is {derangment(i).bottom_up()}')




