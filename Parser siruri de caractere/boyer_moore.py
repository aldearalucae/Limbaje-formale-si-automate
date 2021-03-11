STRING_1_LIMIT = 40
STRING_2_LIMIT = 15_000_000
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def check_limits(string1, string2):
    '''
    Checks strings' lengths
    '''

    if len(string1) >= STRING_1_LIMIT:
        raise Exception(
            f'String1\' s length exceeds its limit: {STRING_1_LIMIT}')

    if len(string2) >= STRING_2_LIMIT:
        raise Exception(
            f'String2\' s length exceeds its limit: {STRING_2_LIMIT}')


def get_delta(string1):
    '''
    Computes delta matrix
    '''

    delta = []
    substrings = [string1[0:i] for i in range(len(string1) + 1)]

    for i, substring in enumerate(substrings):
        line = []

        for letter in ALPHABET:
            if i != len(string1):
                if letter == string1[i]:
                    # Go to next state
                    line.append(i + 1)
                    continue
            # Find best state to continue with
            current_substring = substring + letter

            # Drop first letter if substring's length is bigger than string's length
            if len(current_substring) > len(string1):
                current_substring = current_substring[1:]

            while len(current_substring) >= 0:
                if current_substring == substrings[len(current_substring)]:
                    line.append(len(current_substring))
                    break
                else:
                    current_substring = current_substring[1:]

        # Append the current line
        delta.append(line)

    return delta


def compute_offsets(string1, string2):
    '''
    Computes offsets using Boyer-Moore algorithm
    '''

    offsets = []
    current_state = 0

    # Compute delta
    delta = get_delta(string1)

    for i, letter in enumerate(list(string2)):
        # Update current state using delta matrix
        current_state = delta[current_state][ord(letter) - ord('A')]

        if current_state == len(string1):
            # If final state, save the offset
            offsets.append(i - len(string1) + 1)

    return offsets


def get_offsets(string1, string2):
    '''
    Checks arguments and returns computed offsets
    '''

    # Check limits
    check_limits(string1, string2)

    # Compute and return offsets
    return compute_offsets(string1, string2)
