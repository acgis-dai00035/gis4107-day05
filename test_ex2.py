import ex2
reload(ex2)

def main():
    """main()"""
    expected = True
    x = 2
    y = 2
    xmin = 0
    ymin = 0
    xmax = 3
    ymax = 3
    actual = ex2.is_point_in_box(x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, xmin, ymin, xmax, ymax, expected, actual)

def compare_expected_and_actual(x, y, xmin, ymin, xmax, ymax, expected, actual):
    if expected == actual:
        print 'PASSED:  For x, y, xmin, ymin, xmax, ymax =', x, y, xmin, ymin, xmax, ymax
    else:
        fmt = 'FAILED: For x, y, xmin, ymin, xmax, ymax = {},{},{},{},{},{}\nExpected: {}\nActual:   {}'
        print fmt.format(x, y, xmin, ymin, xmax, ymax, expected, actual)

if __name__ == '__main__':
    main()
