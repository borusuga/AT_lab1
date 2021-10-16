# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : Lab.sm

from utils import statemap


class ParseSMCState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def ClosingBracket(self, fsm):
        self.Default(fsm)

    def Comma(self, fsm):
        self.Default(fsm)

    def Digit(self, fsm, c):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def Letter(self, fsm, c):
        self.Default(fsm)

    def OpenBracket(self, fsm):
        self.Default(fsm)

    def Space(self, fsm):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class Map1_Default(ParseSMCState):

    def Letter(self, fsm, c):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def Digit(self, fsm, c):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def Space(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def OpenBracket(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def Comma(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def ClosingBracket(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def Unknown(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

    def EOS(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Error)
        fsm.getState().Entry(fsm)

class Map1_Start(Map1_Default):

    def ClosingBracket(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isOpenBr() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Map1.BRACKET)
            fsm.getState().Entry(fsm)
        else:
            Map1_Default.ClosingBracket(self, fsm)
        
    def Letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.formType(c)
        finally:
            fsm.setState(Map1.TYPE)
            fsm.getState().Entry(fsm)

class Map1_TYPE(Map1_Default):

    def Digit(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.formType(c)
        finally:
            fsm.setState(Map1.TYPE)
            fsm.getState().Entry(fsm)

    def Letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.formType(c)
        finally:
            fsm.setState(Map1.TYPE)
            fsm.getState().Entry(fsm)

    def Space(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCorrectType() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Map1.SPACE1)
            fsm.getState().Entry(fsm)
        else:
            Map1_Default.Space(self, fsm)
        
class Map1_SPACE1(Map1_Default):

    def Letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Counter()
            ctxt.formFunName(c)
        finally:
            fsm.setState(Map1.FunctionName)
            fsm.getState().Entry(fsm)

class Map1_FunctionName(Map1_Default):

    def ClosingBracket(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCorrectLen() and ctxt.isOpenBr() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Map1.BRACKET)
            fsm.getState().Entry(fsm)
        else:
            Map1_Default.ClosingBracket(self, fsm)
        
    def Comma(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCorrectLen() and ctxt.isOpenBr() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearCounter()
                ctxt.ParCount()
            finally:
                fsm.setState(Map1.SPACE)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Comma(self, fsm)
        
    def Digit(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Counter()
            ctxt.formFunName(c)
        finally:
            fsm.setState(Map1.FunctionName)
            fsm.getState().Entry(fsm)

    def Letter(self, fsm, c):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Counter()
            ctxt.formFunName(c)
        finally:
            fsm.setState(Map1.FunctionName)
            fsm.getState().Entry(fsm)

    def OpenBracket(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCorrectLen() and not ctxt.isOpenBr() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.ClearCounter()
                ctxt.Times()
            finally:
                fsm.setState(Map1.Start)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.OpenBracket(self, fsm)
        
class Map1_BRACKET(Map1_Default):

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.isCorrectLen() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.EOS(self, fsm)
        
class Map1_SPACE(Map1_Default):

    def Space(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Map1.Start)
        fsm.getState().Entry(fsm)

class Map1_OK(Map1_Default):
    pass

class Map1_Error(Map1_Default):

    def ClosingBracket(self, fsm):
        # No actions.
        pass

    def Comma(self, fsm):
        # No actions.
        pass

    def Digit(self, fsm, c):
        # No actions.
        pass

    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(endState)

    def Letter(self, fsm, c):
        # No actions.
        pass

    def OpenBracket(self, fsm):
        # No actions.
        pass

    def Unknown(self, fsm):
        # No actions.
        pass

class Map1(object):

    Start = Map1_Start('Map1.Start', 0)
    TYPE = Map1_TYPE('Map1.TYPE', 1)
    SPACE1 = Map1_SPACE1('Map1.SPACE1', 2)
    FunctionName = Map1_FunctionName('Map1.FunctionName', 3)
    BRACKET = Map1_BRACKET('Map1.BRACKET', 4)
    SPACE = Map1_SPACE('Map1.SPACE', 5)
    OK = Map1_OK('Map1.OK', 6)
    Error = Map1_Error('Map1.Error', 7)
    Default = Map1_Default('Map1.Default', -1)

class ParseSMC_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, Map1.Start)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
