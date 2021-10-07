import datetime
import os
import random

import rstr

TEST_ENDING = '.test'
TYPE = ['int', 'short', 'long']
WRONG_TYPE = ['iNt', 'sHort', 'loNg']
NAME = r"[a-zA-Z][\da-zA-Z]"
WRONG_NAME = r"[\d][\da-zA-Z]"
NOISE = r"[\da-zA-Z \t]"
CPATTERN = r"^(?P<type>int|short|long) (?P<name>[a-zA-Z][\da-zA-Z]{,15})\((((int|short|long) ([a-zA-Z][\da-zA-Z]{,15})\, )*(int|short|long) ([a-zA-Z][\da-zA-Z]{,15}))*\)$"

_ACC = .6
_TRASH = .2
_NACC = .5


def genStr(maxLen):
    if random.random() <= _ACC:  # генерация правильных строк
        tmp = rstr.xeger(CPATTERN)
        tmp = tmp[:maxLen]
        if '(' not in tmp:
            tmp = tmp[:-2] + '()'
        elif ')' not in tmp:
            extra = tmp.split(',')
            if len(extra) == 1:
                tmp = tmp.split('(')[0] + '()'
            else:
                tmp = tmp[:len(tmp) - len(extra[-1]) - 1] + ')'
        return tmp
    elif random.random() <= _TRASH:  # генерация мусора длиной {maxLen/2, maxLen}
        tmp = NOISE + '{' + str(maxLen // 2) + ',' + str(maxLen) + '}'
        return rstr.xeger(tmp)
    else:  # генерация некорректных строк
        wrong = ""
        if random.random() <= _NACC:  # неправильный тип
            wrong += WRONG_TYPE[random.randint(0, len(TYPE) - 1)]
            wrong += ' ' + NAME + '{0,' + str(min(15, maxLen // 2 - 1 - len(wrong))) + '}'
        elif random.random() <= _NACC:  # неправильное имя
            wrong += TYPE[random.randint(0, len(TYPE) - 1)]
            wrong += ' ' + WRONG_NAME + '{0,' + str(min(15, maxLen // 2 - 1 - len(wrong))) + '}'
        else:  # неправильный тип и имя
            wrong += WRONG_TYPE[random.randint(0, len(TYPE) - 1)]
            wrong += ' ' + WRONG_NAME + '{0,' + str(min(15, maxLen // 2 - 1 - len(wrong))) + '}'

        tmp = wrong + '\('

        while len(tmp) + len(wrong) + 3 <= maxLen:
            tmp += wrong + '\, '

        tmp = tmp[:-3] + '\)'

        return rstr.xeger(tmp)


def generate(testDir: str = "./", N: int = 10, maxLen: int = 30):
    tmp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + f"__N{N}__L{maxLen}{TEST_ENDING}"
    path = os.path.join(testDir, tmp)
    with open(path, 'w+', encoding='UTF-8') as out:
        for i in range(N):
            out.write(genStr(maxLen) + '\n')
    return path


# if __name__ == '__main__':
    # if len(sys.argv) != 4:
    #     print("Incorrect argv number")
    #     sys.exit(1)
    # else:
    # path = generate(N=10, maxLen=100)  # (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    # print(f"Done. Saved at {path}")
    # for i in range(100):
    #   print(genStr(250))
    #   print(rstr.xeger(CPATTERN))
