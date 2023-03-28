#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None
    return (result)
