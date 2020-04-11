# Count Derangements with memory optimizations
# Author:: Pavan Kumar Paluri


class arrangement:
    def __init__(self, set_size):
        self.set_size = set_size
        '''
        We need not have an entire array all the time, all we need to access 
        at a given time instance is nth, n-1th, n-2th locations which can 
        be easily achieved by just having 3 variables that store these 3 values
        '''
        self.value_n, value_n_minus_1, value_minus_2 = 0, 0, 0
        for i in range(1, self.set_size+1):
            if i == 1:
                self.value_n = 0
            elif i == 2:
                self.value_n = 1
            else:
                self.value_n = (i - 1) * (value_n_minus_1 + value_minus_2)
            # Rotation phase
            value_minus_2 = value_n_minus_1
            value_n_minus_1 = self.value_n

    def arrange(self):
        return self.value_n


if __name__ == '__main__':
    for i in range(0, 64):
        print(f'result of {i} is {arrangement(i).arrange()}')
