import numpy as np
from time import process_time_ns as ns



def main(*args):
  v = np.random.randint(1, 10000, 10000)
  s = sorted(v)
  r = sorted(v, reverse=True)

  n1 = ns()
  n = sort(s)
  n2 = ns()
  print(n2-n1)
 
  n1 = ns()
  n = sort(v)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  n = sort(r)
  n2 = ns()
  print(n2-n1)

if __name__ == '__quick__':
    quick()