import ex3
reload(ex3)

def main():
    """main()"""
    expected = True
    x = 1
    y = 2
    m = 1
    b = 2
    actual = ex3.is_point_on_line(x,y,m,b)
    compare_expected_and_actual(x,y,m,b, expected, actual)

def compare_expected_and_actual(x,y,m,b, expected, actual):
    if expected == actual:
        print 'PASSED:  For x,y,m,b=', x,y,m,b
    else:
        fmt = 'FAILED: For x,y,m,b = {},{},{},{}\nExpected: {}\nActual:   {}'
        print fmt.format(x,y,m,b, expected, actual)

if __name__ == '__main__':
    main()