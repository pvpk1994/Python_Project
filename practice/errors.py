# Customise Errors
# Inherit from Typerror func


class MyCustomError(Exception):
    """
     Exception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f'Error Code {code}: {message}')
        self.code = code


err = MyCustomError('An Error Occurred', 500)
print(err)
# We also have the option to print the comments in the function we are calling like this:
print(err.__doc__)


# ---- Udemy Exercise Problem : Raising our Own Custom Errors -----------------------
class UncountableError(ValueError):
    def __init__(self, wrong_val):
        super().__init__(f'Invalid value for n, {wrong_val}. n must be greater than 0.')
        self.wrong_val = wrong_val


def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


count_from_zero_to_n(-3)

# ----------------------------------------------------------------------------------


