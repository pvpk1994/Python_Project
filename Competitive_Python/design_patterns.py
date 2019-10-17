'''
Star Designed Patterns
Author: Pavan Kumar Paluri
'''


def star_pattern(num: int):
    for i in range(0, int(num/2)):
        for j in range(0, i+1):
            print('* ', end='\a')
        print('\r')
    # print('Hi')
    for i in range(int(num/2)-1, 0, -1):
        for j in range(0, i+1):
            print('* ', end='\a')
        print('\r')


if __name__ == '__main__':
    star_pattern(16)