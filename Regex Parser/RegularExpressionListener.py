# Generated from RegularExpression.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegularExpressionParser import RegularExpressionParser
else:
    from RegularExpressionParser import RegularExpressionParser

# This class defines a complete listener for a parse tree produced by RegularExpressionParser.
class RegularExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by RegularExpressionParser#starExpr.
    def enterStarExpr(self, ctx:RegularExpressionParser.StarExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#starExpr.
    def exitStarExpr(self, ctx:RegularExpressionParser.StarExprContext):
        pass


    # Enter a parse tree produced by RegularExpressionParser#symStarExpr.
    def enterSymStarExpr(self, ctx:RegularExpressionParser.SymStarExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#symStarExpr.
    def exitSymStarExpr(self, ctx:RegularExpressionParser.SymStarExprContext):
        pass


    # Enter a parse tree produced by RegularExpressionParser#orExpr.
    def enterOrExpr(self, ctx:RegularExpressionParser.OrExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#orExpr.
    def exitOrExpr(self, ctx:RegularExpressionParser.OrExprContext):
        pass


    # Enter a parse tree produced by RegularExpressionParser#symbolExpr.
    def enterSymbolExpr(self, ctx:RegularExpressionParser.SymbolExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#symbolExpr.
    def exitSymbolExpr(self, ctx:RegularExpressionParser.SymbolExprContext):
        pass


    # Enter a parse tree produced by RegularExpressionParser#parenExpr.
    def enterParenExpr(self, ctx:RegularExpressionParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#parenExpr.
    def exitParenExpr(self, ctx:RegularExpressionParser.ParenExprContext):
        pass


    # Enter a parse tree produced by RegularExpressionParser#concatExpr.
    def enterConcatExpr(self, ctx:RegularExpressionParser.ConcatExprContext):
        pass

    # Exit a parse tree produced by RegularExpressionParser#concatExpr.
    def exitConcatExpr(self, ctx:RegularExpressionParser.ConcatExprContext):
        pass



del RegularExpressionParser