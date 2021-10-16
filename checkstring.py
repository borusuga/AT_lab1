import sys

from Parsers import ParseRegex, ParseLeX, ParseSMC

from stringGenerator import generate


def checkSMC(s: str):
    parser = ParseSMC.ParseSMC()
    flag, fun = parser.parse(s)
    if not flag:
        print('The string "{string}" is not acceptable.\n'.format(string=s, result=res))
        return None
    else:
        print('The string "{string}" is acceptable.\n'.format(string=s, result=res))
        return fun


def checkLeX(s: str):
    parser = ParseLeX.ParseLeX()
    parser.build()
    flag, fun = parser.parse(s)
    if not flag:
        print('The string "{string}" is not acceptable.\n'.format(string=s, result=res))
        return None
    else:
        print('The string "{string}" is acceptable.\n'.format(string=s, result=res))
        return fun


def checkRegex(s: str):
    parser = ParseRegex.RegexParser()
    flag, fun = parser.parse(s)
    if not flag:
        print('The string "{string}" is not acceptable.\n'.format(string=s, result=res))
        return None
    else:
        print('The string "{string}" is acceptable.\n'.format(string=s, result=res))
        return fun


if __name__ == "__main__":
    """Finds correct functions with three different ways."""
    retcode = 0
    functions = {}
    print('''Choose input type:
            1.  Keyboard
            2.  File
            3.  Auto String Generator''')
    res = int(input())
    text = ""
    if res == 1:
        print("Enter strings: ")
        text = sys.stdin.read()
    elif res == 2:
        print("Enter name of file: ")
        fname = input()
        handler = open(fname, 'r')
        text = handler.read()
    else:
        test_dir = "./data/"
        # path = generate(test_dir, N=10, maxLen=100)
        path = generate(test_dir, N=1000, maxLen=10)
        handler = open(path, 'r')
        text = handler.read()

    print('''Choose parser:
        1.  SMC
        2.  LeX
        3.  Regex''')
    res = int(input())

    for each in text.split('\n'):
        if res == 1:
            fun_name = checkSMC(each)
        elif res == 2:
            fun_name = checkLeX(each)
        else:
            fun_name = checkRegex(each)
        if fun_name is not None:
            if fun_name not in functions:
                functions[fun_name] = 1
            else:
                functions[fun_name] += 1
        retcode = 1

    print("Acceptable functions: ", functions)
    sys.exit(retcode)
