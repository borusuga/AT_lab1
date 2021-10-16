from utils import Lab_sm


class ParseSMC:
    types = ["int", "long", "short"]
    count = 0  # number of letters
    times = 0  # number of '('
    params = 0
    buff = ""
    fun_name = ""

    def __init__(self):
        self._fsm = Lab_sm.ParseSMC_sm(self)
        self._is_acceptable = False

    def parse(self, string):
        self._fsm.enterStartState()
        for c in string:
            if c.isalpha():
                self._fsm.Letter(c)
            elif c.isdigit():
                self._fsm.Digit(c)
            elif c == '(':
                self._fsm.OpenBracket()
            elif c == ',':
                self._fsm.Comma()
            elif c == ')':
                self._fsm.ClosingBracket()
            elif c == ' ':
                self._fsm.Space()
            else:
                self._fsm.Unknown()

        self._fsm.EOS()

        return self._is_acceptable, self.fun_name

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def Counter(self):
        self.count += 1

    def isCorrectLen(self):
        return self.count <= 16

    def ClearCounter(self):
        self.count = 0

    def Times(self):
        self.times += 1

    def isOpenBr(self):
        return self.times > 0

    def ParCount(self):
        self.params += 1

    def isCorrectType(self):
        if self.buff in self.types:
            self.buff = ""
            return True
        return False

    def formType(self, c: str):
        self.buff += c

    def formFunName(self, c: str):
        if self.times == 0:
            self.fun_name += c
