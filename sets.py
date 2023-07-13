X = set('spam')     # Creates the set {'s', 'p', 'a', 'm'}
Y = {'h', 'a', 'm'}

X, Y        # ({'s', 'p', 'a', 'm'}, {'h', 'a', 'm'}) A tuple of two sets.
X & Y       # {'m', 'a'} Intersection of sets.
X | Y       # {'m', 'h', 'a', 'p', 's'} Union of sets.
X - Y       # {'p', 's'} Difference of sets.