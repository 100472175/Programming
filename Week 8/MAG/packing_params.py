def maximum(*param: int) -> int:  # A Any number of parameters will be accepted
    maxim = param[0]
    for e in param:
        if e > maxim:
            maxim = e
    return maxim

# The * can be used also as: for all elements
