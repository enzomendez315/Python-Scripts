example = "Beautiful!"

len(example)    # Returns 10. Length of string.

example[0]      # 'B'
example[1]      # 'e'

example[-1]     # '!' Last item of string.
example[-2]     # 'l' Second last item of string.

example[1:4]    # 'eau' Slice of string from 1 through 3 (not 4).
example[1:]     # 'eautiful!' Everything past the first char.
example[:3]     # 'ea' Same as example[0:3].

example * 2     # 'Beautiful!Beautiful!' Repetition

example.find('tiful')   # The index of the starting char to be found.
example.replace('eau', 'un')    # 'Buntiful!' Replaces ocurrences.


line = 'aaa,bbb,ccc,ddd'
line.split(',')     # ['aaa', 'bbb', 'ccc', 'ddd'] Splits on a delimiter.

line = 'aaa,bbb,ccc,ddd\n'
line.strip()    # 'aaa,bbb,ccc,ddd' Removes whitespace.

line.strip().split(',') # ['aaa', 'bbb', 'ccc', 'ddd'] Splits and removes whitespace.

'This string %s a formatting %s' % ('contains', 'rule') # 'This string contains a formatting rule'.