def main():
    """main()"""

def is_divisible (numerator,denominator):
    """Given two integers numerator,denominator,
       This function will return true if the numerator is divisible by the denominator with no remainder.
    """
    if isinstance(numerator,int) and isinstance(denominator,int) and numerator > 0 and denominator > 0 :
        if  numerator % denominator == 0 :
            return True
        else :
            return False
    else :
        return 'False'

if __name__ == '__main__':
    main()
