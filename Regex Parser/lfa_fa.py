class FA(object):
    """
    Interface which abstracts the components of a (Nondeterministic or Deterministic) Finite automaton
    """

    def __init__(self, filename, start_state=0):
        """
        Reads and parses a file which contains a Finite automaton
        """

        with open(filename, 'rt') as fin:
            self.start_state = start_state
            self.symbols = set()
            self.states_count = int(fin.readline())
            self.final_states = set(
                map(lambda e: int(e), fin.readline().split()))

            self.read_delta(fin)

    def read_delta(self, fin):
        """
        Reads and parses states' configurations
        """

        raise Exception("Function read_deltas should be implemented!")
