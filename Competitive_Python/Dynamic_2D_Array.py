'''
Dynamic 2D array
Author: Pavan Kumar paluri
Source: Hacker Rank
'''


def dynamicArray(n, queries):
    last_ans = 0
    seq_list = []
    for _ in range(n):
        seq_list.append([])
    for i in range(len(queries)):
        # print(queries[i][0])
        if queries[i][0] == 1:
            seq_index = (queries[i][1] ^ last_ans) % n
            seq_list[seq_index].append(queries[i][2])
            # print(seq_list[seq_index])
        else:
            seq_index = (queries[i][1] ^ last_ans) % n
            # print(seq_index)
            # print(len(seq_list[seq_index]))
            # last_ans = seq_list[queries[i][2] % len(seq_list[seq_index])][queries[i][2]]
            last_ans = seq_list[seq_index][queries[i][2] % len(seq_list[seq_index])]
            print(last_ans)


if __name__ == '__main__':
    first_input = input().rstrip().split()
    n = int(first_input[0])
    q = int(first_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    dynamicArray(n, queries)