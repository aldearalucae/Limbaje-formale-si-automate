from lfa_fa import FA

SYMBOL_EPS = "eps"


class NFA(FA):
    """
    Class which abstracts the components of a Nondeterministic finite automaton
    """

    def __init__(self):
        self.deltas = dict()

    def nfaConcatExpr(self, left_nfa, right_nfa):
        self.start_state = 0
        self.states_count = left_nfa.states_count + right_nfa.states_count
        self.symbols = left_nfa.symbols.union(
            right_nfa.symbols).union(set([SYMBOL_EPS]))
        self.final_states = set([self.states_count - 1])

        for (start_state, symbol), next_states in left_nfa.deltas.items():
            self.deltas[(start_state, symbol)] = next_states

        offset = left_nfa.states_count
        for (start_state, symbol), next_states in right_nfa.deltas.items():
            next_states = set([state + offset for state in next_states])
            self.deltas[(start_state + offset, symbol)] = next_states

        self.deltas[(left_nfa.states_count - 1, SYMBOL_EPS)
                    ] = set([0 + offset])

    def nfaOrExpr(self, left_nfa, right_nfa):
        self.start_state = 0
        self.states_count = left_nfa.states_count + right_nfa.states_count
        self.symbols = left_nfa.symbols.union(
            right_nfa.symbols).union(set([SYMBOL_EPS]))
        self.final_states = set([self.states_count + 1])

        for (start_state, symbol), next_states in left_nfa.deltas.items():
            next_states = set([state + 1 for state in next_states])
            self.deltas[(start_state + 1, symbol)] = next_states

        offset = left_nfa.states_count + 1
        for (start_state, symbol), next_states in right_nfa.deltas.items():
            next_states = set([state + offset for state in next_states])
            self.deltas[(start_state + offset, symbol)] = next_states

        self.deltas[(0, SYMBOL_EPS)] = set([1, offset])
        self.deltas[(left_nfa.states_count, SYMBOL_EPS)] = set(
            [left_nfa.states_count + right_nfa.states_count + 1])
        self.deltas[(left_nfa.states_count + right_nfa.states_count, SYMBOL_EPS)
                    ] = set([left_nfa.states_count + right_nfa.states_count + 1])

        self.states_count = left_nfa.states_count + right_nfa.states_count + 2

    def nfaSymbolExpr(self, symbol):
        self.start_state = 0
        self.states_count = 2
        self.symbols = set([symbol])
        self.final_states = set([1])
        self.deltas[(0, symbol)] = set([1])

    def nfaStarExpr(self, expr_nfa):
        expr_nfa.write('ceva.out')
        self.start_state = 0
        self.states_count = expr_nfa.states_count
        self.symbols = expr_nfa.symbols.union(set([SYMBOL_EPS]))
        self.final_states = set([self.states_count + 1])

        self.deltas[(0, SYMBOL_EPS)] = set([self.states_count + 1, 1])
        self.deltas[(self.states_count, SYMBOL_EPS)] = set(
            [self.states_count + 1, 1])

        for (start_state, symbol), next_states in expr_nfa.deltas.items():
            next_states = set([state + 1 for state in next_states])

            if (start_state, symbol) in self.deltas:
                self.deltas[(start_state + 1, symbol)
                            ] = self.deltas[(start_state, symbol)].union(next_states)
            else:
                self.deltas[(start_state + 1, symbol)] = next_states

        self.states_count = expr_nfa.states_count + 2

    def write(self, filename):
        """
        Writes into the output file the current configurations
        """

        with open(filename, 'wt') as fout:
            # Write number of states
            fout.write(f'{self.states_count}\n')

            # Write final states
            fout.write(
                f"{' '.join(list(map(lambda e: str(e), self.final_states)))}\n")

            # Write deltas
            for (start_state, symbol), final_states in self.deltas.items():
                fout.write(
                    f'{start_state} {symbol} {" ".join(list(map(str,final_states)))}\n')
