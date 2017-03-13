
def get_file_size(file_name):
    """
    :rtype numeric: the number of bytes in a file
    """
    bytes = os.path.getsize(file_name)
    return humanize_bytes(bytes)


def humanize_bytes(bytes, precision=1):
    """Return a humanized string representation of a number of bytes."""
    # This was stollen from http://code.activestate.com/recipes/577081/
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'

    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)


def get_file_line_count(filename):
    """ Return the number of lines in a file
    The idea is to simumalate a `while` loop by reading and returning
    pices of the file in a buffer, and counting `\n` characters
    """
    # Stollen from SO/questions/845058/how-to-get-line-count-cheaply-in-python
    from itertools import (takewhile, repeat)
    with open(filename, 'rb') as f:
        # Make an iterator that returns elements from
        # the iterable as long as the predicate is true:
        #   takewhile(predicate, iterable)
        fragment_iter = takewhile(lambda frag: frag,
                                  (f.raw.read(1024 * 1024)
                                   for _ in repeat(None)))
        return sum(frag.count(b'\n') for frag in fragment_iter)
