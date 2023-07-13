dict = {'food': 'pizza', 'quantity': 4, 'color': 'blue'}

dict['color']   # Returns 'blue'. Gets value of key.
dict['quantity'] += 1   # Returns 5. Adds 1 to value of key.
dict['name'] = 'Bob'    # Create key/value by assignment.


# A dictionary of dictionaries.
student = {'name': {'first': 'Bob', 'last': 'Smith'},
           'degree': {'major': 'Computer Sscience', 'type': 'BS'}}

student['name']['last']     # 'Smith'