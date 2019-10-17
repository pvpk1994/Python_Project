from operator import itemgetter
'''
Jumping Clouds Game
Author : Pavan Kumar Paluri
Source: HackerRank
'''
'''
Description: 
mma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1/2 . 
She must avoid the thunderheads. 
Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. 
It is always possible to win the game.
'''

# This function returns the number of steps taken to reach the goal...


def jumping_on_clouds(c):
    last = len(c)-1
    jumps = i = 0
    while i < (last-2):
        i += 2 if c[i+2] == 0 else 1
        jumps += 1
    # adding an extra jump for victory
    return jumps+1


if __name__ == '__main__':
    # Number of clouds
    n = int(input('Enter the number of clouds:'))
    cloud_list = list(map(int, input().rstrip().split()))
    result = jumping_on_clouds(cloud_list)
    # Result is the number of steps taken to reach the final goal
    print(result)