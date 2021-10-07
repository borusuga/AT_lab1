import re

_PATTERN = r"^(?P<type>int|short|long) (?P<name>[a-zA-Z][\da-zA-Z]{,15})\((((int|short|long) ([a-zA-Z][\da-zA-Z]{,15})\, )*(int|short|long) ([a-zA-Z][\da-zA-Z]{,15}))*\)$"

class RegexParser():
    pattern: str

    def __init__(self):
        super().__init__()
        self.pattern = re.compile(_PATTERN)

    def parse(self, inp: str):
        res = self.pattern.match(inp)

        if res is None:
            return False, None

        return True, res.group('name')


# p = RegexParser()
# print(p.parse("int foo()"))
