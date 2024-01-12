"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/11/24
9.1 Do it Twice Function Decorator Assignment, repeat the function twice
"""


def do_twice(func):
    def repeat_function():
        func()
        func()

    return repeat_function()


@do_twice
def say_hello():
    print("Hello!")
