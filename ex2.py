def main():
    """main()"""

def is_point_in_box (x, y, xmin, ymin, xmax, ymax):
    """Given a point and an area(x,y, xmin, ymin, xmax, ymax), to see if it is in the provided area
    """
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax :
        return True
    else :
        return False


if __name__ == '__main__':
    main()