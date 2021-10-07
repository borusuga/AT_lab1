import ply.lex as lex
from ply.lex import Lexer

'''
Шаблон:
TYPE NAME(TYPE1 NAME1, ...)
'''

_TYPES = {'int', 'short', 'long'}


class ParseLeX:
    tokens = (
        'TYPE',
        'NAME',
        'SPACE',
        'OPENBR',
        'CLOSINGBR',
        'COMMA',
    )

    tokens_list = []

    t_SPACE = r'\ '
    t_COMMA = r'\,'
    t_OPENBR = r'\('
    t_CLOSINGBR = r'\)'

    def t_TYPE(self, t):
        r'(int|short|long)'
        return t

    def t_NAME(self, t):
        r'[a-zA-Z][\da-zA-Z]{,15}'
        if not t.value in _TYPES:
            t.value = t.value
            return t

    def t_error(self, t):
        return False

    def build(self, **kwargs):
        self.lexer: Lexer = lex.lex(module=self, **kwargs)
        return self

    def genTokens(self, inp):
        self.lexer.input(inp)
        while True:
            try:
                tok = self.lexer.token()
            except lex.LexError:
                self.clear()
                return False
            if not tok:
                break
            self.tokens_list.append(tok)
            # print(tok)  # проверка
        return self.tokens_list

    def check(self):
        if len(self.tokens_list) < 5:
            return False, None

        token = self.tokens_list.pop(0)
        if token.type != 'TYPE':
            return False, None

        token = self.tokens_list.pop(0)
        if token.type != 'SPACE':
            return False, None

        token = self.tokens_list.pop(0)
        if token.type != 'NAME':
            return False, None

        fun_name = token.value

        token = self.tokens_list.pop(0)
        if token.type != 'OPENBR':
            return False, None

        if len(self.tokens_list) <= 1:
            token = self.tokens_list.pop(0)
            if token.type != 'CLOSINGBR':
                return False, None
        else:
            for i in range(0, (len(self.tokens_list) - 5) // 4):
                token = self.tokens_list.pop(0)
                if token.type != 'TYPE':
                    return False, None

                token = self.tokens_list.pop(0)
                if token.type != 'SPACE':
                    return False, None

                token = self.tokens_list.pop(0)
                if token.type != 'NAME':
                    return False, None

                token = self.tokens_list.pop(0)
                if token.type != 'COMMA':
                    return False, None

                token = self.tokens_list.pop(0)
                if token.type != 'SPACE':
                    return False, None

            token = self.tokens_list.pop(0)
            if token.type != 'TYPE':
                return False, None

            token = self.tokens_list.pop(0)
            if token.type != 'SPACE':
                return False, None

            token = self.tokens_list.pop(0)
            if token.type != 'NAME':
                return False, None

            token = self.tokens_list.pop(0)
            if token.type != 'CLOSINGBR':
                return False, None
        return True,  fun_name

    def parse(self, inp: str):
        self.clear()
        self.genTokens(inp)
        return self.check()


    def clear(self):
        self.tokens_list.clear()

# pars = ParseLeX()
# pars.build()
# print(pars.parse("int foo()"))
