"""A collection of useful functions.

The template and this example uses Google style docstrings as described at:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

from collections.abc import Iterator


def example_function(number1: int, number2: int) -> str:
    """Compare two integers.

    This is merely an example function can be deleted. It is used to show and test generating
    documentation from code, type hinting, testing, and testing examples
    in the code.


    Args:
        number1: The first number.
        number2: The second number, which will be compared to number1.

    Returns:
        A string describing which number is the greatest.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> example_function(1, 2)
        1 is less than 2

    """
    if number1 < number2:
        return f"{number1} is less than {number2}"

    return f"{number1} is greater than or equal to {number2}"


def darglint_excess_parameter(number1: int) -> int:
    """Extra argument in docstring.

    This triggers DAR102 in darglint, but ruff does not detect it.

    Args:
        number1: The first number.
        number2: An extra number not in the function signature.

    Returns:
        The first number.
    """
    return number1


def darglint_missing_return(number1: int) -> int:
    """Missing return in docstring.

    This triggers DAR201 in darglint, but ruff does not detect it.

    Args:
        number1: The first number.
    """
    return number1


def darglint_excess_return(number1: int) -> None:
    """Extra return in docstring.

    This triggers DAR202 in darglint, but ruff does not detect it.

    Args:
        number1: The first number.

    Returns:
        None.
    """
    print(number1)


def darglint_type_mismatch(number1: int) -> int:
    """Type mismatch in docstring.

    This triggers DAR103 in darglint, but ruff does not detect it.

    Args:
        number1 (str): The first number, but docstring says str instead of int.

    Returns:
        The first number.
    """
    return number1


def darglint_missing_yield(number1: int) -> Iterator[int]:
    """Missing yield in docstring.

    This triggers DAR301 in darglint, but ruff does not detect it.

    Args:
        number1: The first number.
    """
    yield number1
