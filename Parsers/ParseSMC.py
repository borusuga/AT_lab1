from utils import Lab1_sm


class ParseSMC:
    count = 0  # number of letters
    times = 0  # number of '('
    params = 0

    def __init__(self):
        self._fsm = Lab1_sm.ParseSMC_sm(self)
        self._is_acceptable = False

    def parse(self, string):
        self._fsm.enterStartState()
        flag = 0
        fun_name = ""
        for c in string:
            if flag == 1 and c != '(':
                fun_name += c
            if c == 'i':
                self._fsm.Letter_I()
            elif c == 's':
                self._fsm.Letter_S()
            elif c == 'l':
                self._fsm.Letter_L()
            elif c == 'n':
                self._fsm.Letter_N()
            elif c == 't':
                self._fsm.Letter_T()
            elif c == 'h':
                self._fsm.Letter_H()
            elif c == 'o':
                self._fsm.Letter_O()
            elif c == 'r':
                self._fsm.Letter_R()
            elif c == 'g':
                self._fsm.Letter_G()
            elif c.isalpha():
                self._fsm.Letter()
            elif c.isdigit():
                self._fsm.Digit()
            elif (c == '(') and (self.count <= 16) and (self.times == 0):
                self._fsm.OpenBracket()
                flag += 1
            elif (c == ',') and (self.count <= 16) and (self.times > 0):
                self._fsm.Comma()
            elif (c == ')') and (self.count <= 16) and (self.times > 0):
                self._fsm.ClosingBracket()
            elif c == ' ':
                flag += 1
                self._fsm.Space()
            else:
                self._fsm.Unknown()

        self._fsm.EOS()

        return self._is_acceptable,  fun_name

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def Counter(self):
        self.count += 1

    def ClearCounter(self):
        self.count = 0

    def Times(self):
        self.times += 1

    def ParCount(self):
        self.params += 1
