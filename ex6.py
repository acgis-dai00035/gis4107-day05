
def main():
    """main()"""

def is_numeric (test_string):
    """Given a string "test_string" to test if it is a positive or negative whole number (no decimals)
    """
    if isinstance(test_string,str) :
        if test_string.isdigit() :
            return True
        else :
            return False
    else :
        return False


if __name__ == '__main__':
    main()
