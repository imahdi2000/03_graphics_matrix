from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
color2 = [255,0,0]
matrix = new_matrix()

def run():
  edges = new_matrix(4,4);
  add_edge(edges, 50, 450, 0, 100, 450, 0)
  add_edge(edges, 50, 450, 0, 50, 400, 0)
  add_edge(edges, 100, 450, 0, 100, 400, 0)
  add_edge(edges, 100, 400, 0, 50, 400, 0)

  add_edge(edges, 200, 450, 0, 250, 450, 0)
  add_edge(edges, 200, 450, 0, 200, 400, 0)
  add_edge(edges, 250, 450, 0, 250, 400, 0)
  add_edge(edges, 250, 400, 0, 200, 400, 0)

  add_edge(edges, 150, 400, 0, 130, 360, 0)
  add_edge(edges, 150, 400, 0, 170, 360, 0)
  add_edge(edges, 130, 360, 0, 170, 360, 0)

  add_edge(edges, 100, 340, 0, 200, 340, 0)
  add_edge(edges, 100, 320, 0, 200, 320, 0)
  add_edge(edges, 100, 340, 0, 100, 320, 0)
  add_edge(edges, 200, 340, 0, 200, 320, 0)
  draw_lines(edges,screen,color)
  print"Phase 1-----------------------------------------"
  print "Matrix 1"
  print_matrix(edges)
  m = ident(edges)
  print "Identity"
  print_matrix(m)
  z = matrix_mult(m,edges)
  print "Testing Identity and Multiplication"
  print_matrix(z)
  print"DONE Phase 1-----------------------------------------"
  print""
  print"Phase 2-----------------------------------------"
  wow = new_matrix(1,4)
  add_edge(wow,2,5,6,7,8,9)
  add_edge(wow,2,5,6,7,8,9)
  print "Matrix 1"
  print_matrix(wow)
  now = new_matrix(1,4)
  add_edge(now,2,5,6,7,8,9)
  add_point(now,2,5,6)
  print "Matrix 2"
  print_matrix(now)
  print "Multiply Result"
  qq = matrix_mult(wow,now)
  print_matrix(qq)
  print"DONE Phase 2-----------------------------------------"




run()
'''draw_lines( matrix, screen, color )'''
display(screen)
