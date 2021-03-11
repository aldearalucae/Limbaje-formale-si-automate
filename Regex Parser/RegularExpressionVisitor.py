# Generated from RegularExpression.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegularExpressionParser import RegularExpressionParser
else:
    from RegularExpressionParser import RegularExpressionParser

# This class defines a complete generic visitor for a parse tree produced by RegularExpressionParser.

class RegularExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegularExpressionParser#starExpr.
    def visitStarExpr(self, ctx:RegularExpressionParser.StarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegularExpressionParser#symStarExpr.
    def visitSymStarExpr(self, ctx:RegularExpressionParser.SymStarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegularExpressionParser#orExpr.
    def visitOrExpr(self, ctx:RegularExpressionParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegularExpressionParser#symbolExpr.
    def visitSymbolExpr(self, ctx:RegularExpressionParser.SymbolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegularExpressionParser#parenExpr.
    def visitParenExpr(self, ctx:RegularExpressionParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegularExpressionParser#concatExpr.
    def visitConcatExpr(self, ctx:RegularExpressionParser.ConcatExprContext):
        return self.visitChildren(ctx)



del RegularExpressionParser