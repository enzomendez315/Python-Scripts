my_tuple = (1, 2, 3, 4)

len(my_tuple)       # Returns 4.
my_tuple + (5, 6)   # (1, 2, 3, 4, 5, 6) Returns a new tuple since they're immutable.
my_tuple[0]         # Returns 1. Returns item at index 0.
my_tuple.index(4)   # Returns 3. Returns first index of value.
my_tuple.count(4)   # Returns 1. Returns how often the value is repeated.
(2,) + my_tuple[1:]     # (2, 2, 3, 4) Returns a new tuple.