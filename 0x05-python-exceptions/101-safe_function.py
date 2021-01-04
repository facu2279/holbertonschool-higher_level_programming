#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as error:
        print("Exception: {0}".format(error), file=sys.stderr)
        return
    return res
