'''
Python script to calculate context switch time from a xentrace log
Author: Pavan Kumar Paluri
Copyright @ 2020 - RTLAB at University of Houston
'''

import sys

if __name__ == '__main__':
    # Get 1st arg as file name
    file_name = sys.argv[1]
    prev_context_switch = 0
    context_switch_counter = 0
    actual_context_switches = []
    with open(file_name, "r") as file_opt:
        # Read line after line
        line = file_opt.readline()
        while line:
            word_after_split = line.split('  ')
            # extract only 9 and 10 domain rows
            if (word_after_split[2] == '\'1\': 9' or word_after_split[2] == '\'1\': 10')\
                    and (word_after_split[3] == '\'3\': 9' or word_after_split[3] == '\'3\': 10'):
                tsc_value = word_after_split[1].split(': ')
                context_switch_counter += 1
                if prev_context_switch == 0:
                    prev_context_switch = int(tsc_value[1])
                    line = file_opt.readline()
                    continue
                diff_context_switch = int(tsc_value[1]) - prev_context_switch
                # gather all the context switch times into a list
                # arbitrary param set: 15000
                actual_context_switches.append(diff_context_switch)
                # If here, set prev_context_switch to be an updated val for next line diff
                prev_context_switch = int(tsc_value[1])
            else:
                # if the sequence breaks, reset context switch
                prev_context_switch = 0
            line = file_opt.readline()
    # pop the fist elem of the list
    actual_context_switches.pop(0)
    print(f'Context switch typical time exclusively for RTDS domains: {actual_context_switches[len(actual_context_switches)-1]}')

    # Get various stats from the list of context switches obtained
    # Print Number of the Context switches
    print(f'Number of context switches: {context_switch_counter}')

    # Only print the head of the list for verification purposes.

    print(f'Context switch list head: {actual_context_switches[0]}')
