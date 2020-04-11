'''
Text Justification Using Brute Force Approach
Author: Pavan Kumar Paluri
'''
import sys # for setting the max value (inf)

class text_justify:
    def __init__(self, text, line_max_length):
        self.text = text
        self.line_max_length = line_max_length

    def ugly_score(self, text_length):
        '''
        Takes in the text length and returns the ugly score value
        :param text_length: int
        :return: ugly score
        '''
        if text_length <= self.line_max_length:
            return (self.line_max_length - text_length) ** 2
        else: # if the text length exceeds line's max_length
            return sys.maxsize

    def count_chars_include_spaces(self, fro, to):
        total_char_counter = 0
        for i in range(fro, to):
            total_char_counter += len(self.text[i])
            # add a space at the end of each iteration
            # for last word, do not add a space
            if i < to-1:
                total_char_counter += 1
        return total_char_counter

    # this is the recurrence / recursive function
    def recurrence_relation(self, index):
        # Establish a stopping condition
        if index == len(self.text):
            return 0
        score = sys.maxsize
        for x in range(index+1, len(self.text)+1):
            line_tot_len = self.count_chars_include_spaces(index, x)
            current_score = self.ugly_score(line_tot_len)
            current_score += self.recurrence_relation(x)
            score = min(current_score, score)
        return score


if __name__ == '__main__':
    txt_justify = text_justify("Pavan Kumar Paluri sat on the Plane".split(), 10)
    # Printing the optimised ugly score
    print(txt_justify.recurrence_relation(0))

