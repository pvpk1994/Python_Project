'''
Source: Hacker Rank
Author: Pavan Kumar Paluri
Count #of a's in an infinite repetitive string
'''


def repeatedString(s, n):
    # Indefinite repeating string..
    s = s.strip()
    perfect_slice = s.count("a") * (n // len(s))
    rem_slice = s[:n % len(s)].count("a")
    return perfect_slice + rem_slice


if __name__ == '__main__':
    s = input()
    n = int(input())
    print(repeatedString(s, n))