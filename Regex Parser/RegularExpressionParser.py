# Generated from RegularExpression.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("\33\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\r\n\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write("\2\3\2\2\3\2\3\2\2\2\2\36\2\f\3\2\2\2\4\5\b\2\1\2\5\6")
        buf.write("\7\3\2\2\6\r\7\6\2\2\7\b\7\4\2\2\b\t\5\2\2\2\t\n\7\5\2")
        buf.write("\2\n\r\3\2\2\2\13\r\7\3\2\2\f\4\3\2\2\2\f\7\3\2\2\2\f")
        buf.write("\13\3\2\2\2\r\27\3\2\2\2\16\17\f\5\2\2\17\26\5\2\2\6\20")
        buf.write("\21\f\4\2\2\21\22\7\7\2\2\22\26\5\2\2\5\23\24\f\3\2\2")
        buf.write("\24\26\7\6\2\2\25\16\3\2\2\2\25\20\3\2\2\2\25\23\3\2\2")
        buf.write("\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2")
        buf.write("\2\2\31\27\3\2\2\2\5\f\25\27")
        return buf.getvalue()


class RegularExpressionParser ( Parser ):

    grammarFileName = "RegularExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'*'", "'|'" ]

    symbolicNames = [ "<INVALID>", "SYMBOL", "LPAREN", "RPAREN", "STAR", 
                      "OR" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    SYMBOL=1
    LPAREN=2
    RPAREN=3
    STAR=4
    OR=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegularExpressionParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegularExpressionParser.ExprContext,0)

        def STAR(self):
            return self.getToken(RegularExpressionParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStarExpr" ):
                listener.enterStarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStarExpr" ):
                listener.exitStarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStarExpr" ):
                return visitor.visitStarExpr(self)
            else:
                return visitor.visitChildren(self)


    class SymStarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.symb = None # Token
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(RegularExpressionParser.STAR, 0)
        def SYMBOL(self):
            return self.getToken(RegularExpressionParser.SYMBOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymStarExpr" ):
                listener.enterSymStarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymStarExpr" ):
                listener.exitSymStarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymStarExpr" ):
                return visitor.visitSymStarExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(RegularExpressionParser.OR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegularExpressionParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegularExpressionParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class SymbolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.symb = None # Token
            self.copyFrom(ctx)

        def SYMBOL(self):
            return self.getToken(RegularExpressionParser.SYMBOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolExpr" ):
                listener.enterSymbolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolExpr" ):
                listener.exitSymbolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbolExpr" ):
                return visitor.visitSymbolExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(RegularExpressionParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(RegularExpressionParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(RegularExpressionParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConcatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegularExpressionParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegularExpressionParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegularExpressionParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpr" ):
                listener.enterConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpr" ):
                listener.exitConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpr" ):
                return visitor.visitConcatExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegularExpressionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = RegularExpressionParser.SymStarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                localctx.symb = self.match(RegularExpressionParser.SYMBOL)
                self.state = 4
                self.match(RegularExpressionParser.STAR)
                pass

            elif la_ == 2:
                localctx = RegularExpressionParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(RegularExpressionParser.LPAREN)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(RegularExpressionParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = RegularExpressionParser.SymbolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                localctx.symb = self.match(RegularExpressionParser.SYMBOL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = RegularExpressionParser.ConcatExprContext(self, RegularExpressionParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 13
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = RegularExpressionParser.OrExprContext(self, RegularExpressionParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 15
                        self.match(RegularExpressionParser.OR)
                        self.state = 16
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = RegularExpressionParser.StarExprContext(self, RegularExpressionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 18
                        self.match(RegularExpressionParser.STAR)
                        pass

             
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




