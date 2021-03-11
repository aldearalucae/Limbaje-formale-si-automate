import sys
from lfa_nfa import *
from antlr4 import *
from lfa_dfa import *
from RegularExpressionLexer import RegularExpressionLexer
from RegularExpressionVisitor import RegularExpressionVisitor
from RegularExpressionParser import RegularExpressionParser


def parse_argv():
    """
    Check and parse given arguments
    """

    if len(sys.argv) != 4:
        raise Exception(
            "Usage: python3 main.py <input−file> <output−file-1> <output−file-2>")

    return sys.argv[1], sys.argv[2], sys.argv[3]


class EvalVisitor(RegularExpressionVisitor):
    def visitSymbolExpr(self, ctx):
        nfa = NFA()
        nfa.nfaSymbolExpr(ctx.getText())

        print("visitSymbolExpr", ctx.getText())
        return nfa

    def visitSymStarExpr(self, ctx):
        expr_nfa = NFA()
        expr_nfa.nfaSymbolExpr(ctx.symb.text)

        print("visitSymStarExpr", ctx.getText())

        nfa = NFA()
        nfa.nfaStarExpr(expr_nfa)

        return nfa

    def visitParenExpr(self, ctx):
        nfa = self.visit(ctx.expr())
        print("visitParenExpr", ctx.getText())

        return nfa

    def visitConcatExpr(self, ctx):
        left_nfa = self.visit(ctx.left)
        right_nfa = self.visit(ctx.right)

        nfa = NFA()
        nfa.nfaConcatExpr(left_nfa, right_nfa)

        print("visitConcatExpr", ctx.getText())

        return nfa

    def visitOrExpr(self, ctx):
        left_nfa = self.visit(ctx.left)
        right_nfa = self.visit(ctx.right)
        print("orExpr", ctx.getText())

        # nfa = NFA()
        # nfa.nfaOrExpr(left_nfa, right_nfa)
        
        return right_nfa

    def visitStarExpr(self, ctx):
        expr_nfa = self.visit(ctx.expr())

        print("starExpr", ctx.getText())

        nfa = NFA()
        nfa.nfaStarExpr(expr_nfa)

        return nfa


def main(argv):
    input_filename, output_filename_1, output_filename_2 = parse_argv()

    lexer = RegularExpressionLexer(FileStream(input_filename))
    stream = CommonTokenStream(lexer)
    parser = RegularExpressionParser(stream)
    tree = parser.expr()

    nfa = EvalVisitor().visit(tree)

    nfa.write(output_filename_1)

    dfa = DFA(nfa)

    dfa.write(output_filename_2)


if __name__ == '__main__':
    main(sys.argv)
