#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        result = None
    finally:
        return (result)
