# Lists also support all the sequence operations that strings support.
# See strings.py for details.
my_list = [123, '456', 1.23]

len(my_list)    # Returns 3
my_list[0]      # Returns 123
my_list[:-1]    # [123, '456']
my_list + [7, 8, 9]     # [123, '456', 1.23, 7, 8, 9] Concatenates string.
my_list * 2     # [123, '456', 1.23, 123, '456', 1.23]


# List specific operations
my_list.append('83')    # Adds object to the end of list.
my_list.pop(2)      # [123, '456'] Deletes item at index 2.

letters = ['bb', 'aa', 'cc']
letters.sort()      # ['aa', 'bb', 'cc']
letters.reverse()   # ['cc', 'bb', 'aa']


matrix = [[1, 2, 3],    # A list of lists to represent a matrix.
          [4, 5, 6],
          [7, 8, 9]]

matrix[1]       # [4, 5, 6]
matrix[1][2]    # Returns 6.

[row[1] for row in matrix]  # [2, 5, 8] Grabs column of matrix at index 1.