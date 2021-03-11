from sys import argv
from boyer_moore import get_offsets


def read_input_file(filename):
    '''
    Reads input file
    '''
    string1, string2 = None, None

    try:
        with open(filename, 'rt') as f:
            string1 = f.readline().strip().upper()
            string2 = f.readline().strip().upper()
    except:
        raise Exception('File reading error')

    return string1, string2


def write_output_file(filename, offsets):
    '''
    Writes output file
    '''
    with open(filename, 'wt') as f:
        for offset in offsets:
            f.write(str(offset) + ' ')

        f.write('\n')


if __name__ == '__main__':
    '''
    Main function
    '''

    # Check arguments
    if len(argv) != 3:
        raise Exception('Usage: python main.py input_filename output_filename')

    # Store filenames
    input_filename = argv[1]
    output_filename = argv[2]

    # Read input file
    string1, string2 = read_input_file(input_filename)

    # Compute offsets using Boyer-Moore algorithm
    offsets = get_offsets(string1, string2)

    # Write output file
    write_output_file(output_filename, offsets)
