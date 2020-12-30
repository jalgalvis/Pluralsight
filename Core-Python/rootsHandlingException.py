def sqrt(x):
    """ Compute square roots using the method of
    Heron of Alexandria.

    :arg
        x: the number for which the square root
            is to be computed
    :return
        The square root of x.
    """
    guess = x
    i = 0

    while guess * guess != x and i < 28:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed")
    except ZeroDivisionError:
        print("Cannot compute square root of a negative nnumber")

    print("Program execution continues normally here")


if __name__ == '__main__':
    main()