# Bad
# def f(x):
#     return x*x

# Good
def square(number: int) -> int:
    """Return the square of a number."""
    return number * number

print(square(123))