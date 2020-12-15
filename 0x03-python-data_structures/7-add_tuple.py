#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    largotupla_a = len(tuple_a)
    largotupla_b = len(tuple_b)
    if largotupla_a < 2:
        if largotupla_a < 1:
            aux_a = 0, 0
        else:
            aux_a = tuple_a[0], 0
    else:
        aux_a = tuple_a
    if largotupla_b < 2:
        if largotupla_b < 1:
            aux_b = 0, 0
        else:
            aux_b = tuple_b[0], 0
    else:
        aux_b = tuple_b
    new = aux_a[0] + aux_b[0], aux_a[1] + aux_b[1]
    return new
