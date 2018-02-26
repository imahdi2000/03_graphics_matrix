import math


def print_matrix( matrix ):
    for i in matrix:
            print str(i)
            print "\t"


def ident( matrix ):
    m = new_matrix()
    for row in range(len(m)):
        for col in range(len(m[0])):
            if (row == col):
                m[row][col] = 1
            if (row != col):
                m[row][col] = 0
    return m

#m1 * m2 -> m2
'''Dot product rule: [row of matrix 1] * [column of matrix 2]'''
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m2[0]), len(m2))
    for row1 in range(len(m1)):
        for col2 in range(len(m2[0])):
            for row2 in range(len(m2)):
                m[row1][col2] += m1[row1][row2] * m2[row2][col2]
    for row in range(len(m2)):
        for col in range(len(m2[0])):
            m2[row][col] = m[row][col]
    return m2





def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
