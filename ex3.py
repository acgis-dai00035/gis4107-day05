def main():
    """main()"""

def is_point_on_line (x, y, m, b):
    """Given a point (x,y), to see if it is on the line y=mx+b
    """
    if y == m*x + b :
        return True
    else :
        return False

if __name__ == '__main__':
    main()
