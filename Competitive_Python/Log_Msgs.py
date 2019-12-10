'''
Log Messages Format and printing
Source: Argo AI interview question prototype
Author: Pavan Kumar Paluri
'''


def log_info(str_inp: str, list_arg) -> str:
    i = 0
    char = '{}'

    if len(list_arg) == 2:
        for i in range(len(list_arg)):
            if char in str_inp:
                str_inp = str_inp.replace(char, list_arg[i], 1)
            # i += 1
    elif len(list_arg) == 1:
        if char in str_inp:
            str_inp = str_inp.replace(char, list_arg[i], 1)
    elif len(list_arg) == 0:
        if char in str_inp:
            raise AssertionError('Error encountered')
    # print(f'{list_arg[0]},{list_arg[1]}')
    return '[INFO] ' + str_inp


if __name__ == '__main__':
    list_args = []
    log_msg = input()
    argc = 0
    for _ in range(argc):
        arg1 = input()
        list_args.append(arg1)
    print(f'List arg: {list_args}')
    print(log_info(log_msg, list_args))
