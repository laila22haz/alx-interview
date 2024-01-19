#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n):
    """Copy/Paste"""
    if n <= 1:
        return 0
    
    operation_needed = 0
    clipbord = 0
    current_lenght = 1

    while current_lenght < n:
        # If n is divisible by current length, we can copy all
        if n % current_lenght == 0:
            # This is the only time we can copy
            clipbord = current_lenght
            operation_needed += 1

        current_lenght += clipbord
        operation_needed += 1
    
    return operation_needed


""" n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 10
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
 """