'''
New Year's Problem
Author: Pavan Kumar Paluri
'''


def minimumBribes(Q):
    moves = 0
    Q_new = [P - 1 for P in Q]
    for i, P in enumerate(Q_new):
        print(i, P)
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P - 1, 0), i):
            if Q_new[j] > P:
                moves += 1
    print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        # print("\n")
        minimumBribes(q)
