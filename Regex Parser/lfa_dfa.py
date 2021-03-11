from lfa_fa import FA

SYMBOL_EPS = "eps"


class DFA(FA):
    """
    Class which abstracts the components of a Deterministic finite automaton
    """

    def __init__(self, nfa, start_state=0):
        """
        Converts the given NFA into a DFA
        """

        # Declare FA and DFA fields
        self.start_state = start_state
        self.states_count = 0
        self.final_states = set()
        self.symbols = nfa.symbols
        self.delta = {}

        # Compose closures
        closures = self.closures(nfa)

        # Compose auxiliary delta (middle delta)
        middle_delta = self.middle_delta(nfa, closures)

        # Convert middle delta into delta
        self.compose_delta(middle_delta, nfa)

    def middle_delta(self, nfa, closures):
        """
        Creates a delta auxiliary array
        """

        delta = dict()

        # Set first state
        self.start_state = tuple(set([0]).union(closures[0]))
        states_queue = {self.start_state}
        states_used = []

        while len(states_queue):
            current_state = states_queue.pop()
            states_used.append(set(current_state))

            for symbol in nfa.symbols:
                next_state = set()

                # Consume transitions
                for current_state_id in current_state:
                    if (current_state_id, symbol) in nfa.deltas:
                        next_state = next_state.union(
                            nfa.deltas[(current_state_id, symbol)])

                # Consume eps-closures
                for e in next_state:
                    next_state = next_state.union(closures[e])

                if len(next_state) > 0:
                    # Create new transition
                    delta[(current_state, symbol)] = tuple(next_state)

                    # If state does not exist, it will be created
                    if len(list(filter(lambda e: e == next_state, states_used))) == 0:
                        states_queue.add(tuple(next_state))

        return delta

    def compose_delta(self, middle_delta, nfa):
        """
        Translate a middle_delta into a DFA valid delta
        """

        mappings = {self.start_state: 0}
        self.states_count += 1

        # Maps every transition
        for ((start_state, symbol), next_state) in middle_delta.items():
            start_state_mapping = self.get_mapping(mappings, start_state, nfa)
            next_state_mapping = self.get_mapping(mappings, next_state, nfa)

            self.delta[(start_state_mapping, symbol)] = next_state_mapping

        # Mark final states
        for states, new_state in mappings.items():
            if len(set(states).intersection(nfa.final_states)) > 0:
                self.final_states.add(new_state)

        # Check if extra state is needed
        has_extra_state = False
        extra_state = -1

        for state in range(self.states_count):
            for symbol in self.symbols:
                if (state, symbol) not in self.delta:
                    if not has_extra_state:
                        has_extra_state = True
                        extra_state = self.states_count
                        self.states_count += 1

                    self.delta[(state, symbol)] = extra_state

        if has_extra_state:
            for symbol in self.symbols:
                self.delta[(extra_state, symbol)] = extra_state

    def closures(self, nfa):
        """
        Receives a NFA and computes eps-closures
        """

        closures = dict()

        for state in range(nfa.states_count):
            closure = set()
            next_states = set()
            curr_state = state

            # Do-while for each eps transition from curr_state
            while True:
                if (curr_state, SYMBOL_EPS) in nfa.deltas:
                    next_states = next_states.union(
                        nfa.deltas[(curr_state, SYMBOL_EPS)].difference(closure))

                if len(next_states) == 0:
                    break

                curr_state = next_states.pop()
                closure = closure.union(set([curr_state]))

            # Add new closure
            closures[state] = closure

        # Delete eps transitions
        for state in range(nfa.states_count):
            if (state, SYMBOL_EPS) in nfa.deltas:
                del nfa.deltas[(state, SYMBOL_EPS)]

        # Delete eps from symbols
        if SYMBOL_EPS in nfa.symbols:
            nfa.symbols.remove(SYMBOL_EPS)

        return closures

    def get_mapping(self, mappings, state, nfa):
        """
        Maps a given set of states (called state) into a new state, or into an existing one
        """

        state_mapping = None

        if state in mappings.keys():
            state_mapping = mappings[state]
        else:
            mappings[state] = self.states_count
            state_mapping = self.states_count
            self.states_count += 1

        return state_mapping

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
            for (start_state, symbol), final_state in self.delta.items():
                fout.write(f'{start_state} {symbol} {final_state}\n')
