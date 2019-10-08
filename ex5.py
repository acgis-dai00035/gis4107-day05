def main():
    """main()"""

def is_divisible (numerator,denominator):
    """Given two integers numerator,denominator,
       This function will return true if the numerator is divisible by the denominator with no remainder.
    """
    if  str(numerator).isdigit() and str(denominator).isdigit() and int(numerator) > 0 and int(denominator) > 0:
        if int(numerator) % int(denominator) == 0 :
            return True
        else :
            return False
    else :
        return False

if __name__ == '__main__':
    main()
