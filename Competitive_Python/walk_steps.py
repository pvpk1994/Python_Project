'''
Walk-steps.py
Author: Pavan Kumar Paluri
Source:: Google Interview (Phone)
'''

'''
Description: You start at index 0 in an array with length 'h'. 
At each step, you can move to the left, move to the right, or stay in the same place
(Note! Stay in the same place also takes one step). 
How many possible ways are you still at index 0 after you have walked 'n' step?
'''
'''
Example:
n = 3
1. right->left->stay
2. right->stay->left
3. stay->right->left
4. stay->stay->stay
'''


# Approach 1: Recursion
def walk(position: int, index: int, num_steps: int, height: int) -> int:
    if position < 0 or position >= height:
        return 0
    if index == num_steps and position == 0:
        return 1
    if index == num_steps:
        return 0
    count = 0
    count += walk(position-1, index+1, num_steps, height)
    count += walk(position, index+1, num_steps, height)
    count += walk(position+1, index+1, num_steps, height)

    return count


if __name__ == '__main__':
    print(f'The number of ways: {walk(0, 0, 4, 4)}')
