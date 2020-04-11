'''
Text Justification Memory Optimized
Author: Pavan Kumar Paluri
'''

import sys


class text_justify_dp:
    def __init__(self, txt, line_length):
        self.txt = txt
        self.line_length = line_length
        # Create an empty 2d array
        self.table = [[]]*len(self.txt)
        for i in range(len(self.txt)):
            # Row init
            self.table[i] = [0] * len(self.txt)
            # fill all the diagonal elements with their own lengths
            self.table[i][i] = len(self.txt[i])
            for j in range(i+1, len(self.txt)):
                self.table[i][j] = self.table[i][j-1] + 1 + len(self.txt[j])

        # Print Array for demonstration purposes...
        for arr in self.table:
            print(arr)

    def ugly_score_cal(self, txt_length):
        # Cal ugly score based on the length of the txt
        if txt_length <= self.line_length:
            return (self.line_length - txt_length) ** 2
        else:
            return sys.maxsize


    '''
    # Apply DP approach (Bottom Up solution)
    # Brute Force

    def txt_justify_bottom_up(self, index_from):
        if index_from == len(self.txt):
            return 0
        # Set score to be an infinitely huge value initially
        score = sys.maxsize
        for index_new in range(index_from+1, len(self.txt) + 1):
            len_txt = self.count_total_len_text(index_from, index_new)
            current_score = self.ugly_score_cal(len_txt)
            current_score += self.txt_justify_bottom_up(index_new)
            score = min(current_score, score)
        return score
    '''

    def txt_justify_bottom_up(self):
        # Technique of memoization
        scores = [0]*(len(self.txt) + 1)
        # store array of pointers pointing to the next index
        ptrs = [0]*len(self.txt)

        for i in range(len(self.txt) - 1, -1, -1):
            score = sys.maxsize
            for j in range(i+1, len(self.txt)+1):
                current_score = self.ugly_score_cal(self.table[i][j-1]) + scores[j]
                if current_score < score:
                    score = current_score
                    # Index j holds the location of next ptr to be jumped to..
                    ptrs[i] = j
            scores[i] = score
        self.print_text(ptrs)
        return scores[0]

    def print_text(self, ptrs):
        i = 0
        while i < len(ptrs):
            line = self.txt[i:ptrs[i]]
            print(" ".join(line))
            # To further increment the loop
            i = ptrs[i]


if __name__ == '__main__':
    txt_justify = text_justify_dp("Isabel sat on the step".split(), 10)
    print(txt_justify.txt_justify_bottom_up())
