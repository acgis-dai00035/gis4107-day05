def main():
    """main()"""

def mod_myvar(myvar):
    """Given a number myvar, test if it can pass the test
    """
    if myvar % 2:
        if myvar ** 3 != 27:
            myvar += 4           # myvar = 1 return 5
        else:
            myvar /= 1.5         # myvar = 3 return  2
    else:
        if myvar <= 10:
            myvar *= 2           # myvar = 2 return 4
        else:
            myvar -= 2           # myvar = 12 return 10
    return myvar



if __name__ == '__main__':
    main()
