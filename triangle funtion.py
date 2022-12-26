def triangle(h, o, skip):
    s = 1
    p = h - 1
    skip_count = 0
    for r in range(h):
        if skip_count >= skip:
            print("  " * o + "  " * p + "* " * s)
        s += 2
        p -= 1
        skip_count += 1

triangle(3, 4, 0)  
triangle(5, 2, 1)       # HW: Draw the Christmas tree
triangle(7, 0, 2)  