from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for i in range (0,len(matrix[0]), 2):
        draw_line(matrix[0][i], matrix[1][i],matrix[0][i+1], matrix[1][i+1],screen,color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)

def draw_line( x0, y0, x1, y1, screen, color ):
#check that x0 is bigger than x1
    if (x0 > x1):
        #draw_line( x1, y1, x0, y0, screen, color)
        test = x0
        x0 = x1
        x1 = test
        test = y0
        y0 = y1
        y1 = test
    #check for a point
    if(x0 == x1 and y0 == y1):
        plot(screen, color, x0, y0)

    #change in x (B), change in y (A)
    A = y1 - y0
    B = (-1.0) * (x1 - x0)

    #set initial point
    x = x0
    y = y0

    #check for slope of 0
    if (B == 0):
        if (y < y1):
            while(y <= y1):
                plot(screen, color, x, y)
                y = y + 1
        if (y > y1):
            while(y >= y1):
                plot(screen, color, x, y)
                y = y - 1
        return


    #make a slope, rise over run, y/x
    m = (float(y1-y0) / float(x1-x0))

    #check for octant 1 & 5 using slope
    if (m >= 0 and m <= 1):
        d = (2 * A) + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d = d + (2 * B)
            x = x + 1
            d = d + (2 * A)

    #check for octant 2 & 6
    if (m > 1):
        d = A + (2 * B)
        while (y <= y1):
            plot(screen, color, x,y)
            if (d < 0):
                x = x + 1
                d = d + (2 * A)
            y = y + 1
            d = d + (2 * B)


    # check for  7
    if (m < 0 and m >= -1):
        d = (2 * A) - B
        while (x <= x1):
            plot(screen,color, x,y)
            if (d < 0):
                y = y -1
                d = d - (2 * B)
            x = x + 1
            d = d + (2 * A)

    if (m < -1):
        d = A - (2 * B)
        while (y >= y1):
            plot(screen,color, x,y)
            if (d > 0):
                x = x + 1
                d = d + (2 * A)
            y = y - 1
            d = d - (2 * B)
