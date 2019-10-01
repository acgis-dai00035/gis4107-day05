import ex5
reload(ex5)

def main():
    """main()"""
    expected = True
    numerator = 12
    denominator = 3
    actual = ex5.is_divisible(numerator,denominator)
    compare_expected_and_actual(numerator,denominator, expected, actual)

def compare_expected_and_actual(numerator,denominator, expected, actual):
    if expected == actual:
        print 'PASSED:  For numerator,denominator=', numerator,denominator
    else:
        fmt = 'FAILED: For numerator,denominator = {},{}\nExpected: {}\nActual:   {}'
        print fmt.format(numerator,denominator, expected, actual)

if __name__ == '__main__':
    main()
