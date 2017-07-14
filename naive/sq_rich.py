"""
An attempt to generalize the Fraenkel-Simpson example of
square-dense inifinite words.
"""

import naive as naive
import naive_occ as naive_occ

##########################################
# the original Fraenkel-Simpson construction

def sq_rich(n) :
  """returns the nth intermediate element of the Fraenkel-Simpson construction"""
  s = ""
  bloc0 = "0"
  for _ in range(n) :
    s += bloc0 + "01" + bloc0 + "1" + bloc0 + "01"
    bloc0 += "0"
  return s

def study_of_sq_rich(n, m) :
  """gives information about the square factors from the n-th to the the m-th
  element of the Fraenkel-Simpson construction"""
  word = sq_rich(n)
  bloc0 = "0" * n
  word_len = len(word)
  print("n\tlen\tnb sq\tdefect")
  for i in range(n, m + 1) :
    nb_squares = naive.nb_squares(sq_rich(i))
    print("{}\t{}\t{}\t{}".format(i, word_len, nb_squares, word_len - nb_squares + 1))
    word += bloc0 + "01" + bloc0 + "1" + bloc0 + "01"
    bloc0 += "0"
    word_len += 3 * (i + 1) + 5

##########################################
# the variants

def sq_rich_odd_exponents(n) :
  """a variant of the Fraenkel-Simpson construction with odd-sized series of 0"""
  s = ""
  bloc0 = "0"
  for _ in range(n) :
    s += bloc0 + "001" + bloc0 + "1" + bloc0 + "001"
    bloc0 += "00"
  return s

def sq_rich_of(u, n) :
  """gives the n-th element of the Fraenkel-Simpson construction where
  the exponents are given by the sequence"""
  s = ""
  for i in range(1, n + 1) :
    s += "0" * u(i + 1) + "1" + "0" * u(i) + "1" + "0" * u(i + 1) + "1"
  return s

def sq_rich_study(n, m, u = lambda x : x) :
  """gives information about the square factors from the n-th to the the m-th
  element of any variant of the Fraenkel-Simpson construction"""
  word = sq_rich_of(u, n)
  word_len = len(word)
  u_i = u(n + 1)
  u_i_next = u(n + 2)
  print("n\tlen\tnb sq\tdefect\tdensity")
  for i in range(n, m + 1) :
    nb_squares = naive.nb_squares(word)
    print("{}\t{}\t{}\t{}".format(i, word_len, nb_squares, word_len - nb_squares + 1))
    word += "0" * u_i_next + "1" + "0" * u_i + "1" + "0" * u_i_next + "1"
    word_len += 2 * u_i + u_i_next + 2
    u_i = u_i_next
    u_i_next = u(i + 3)

##########################################
# some integer sequences

def fibo(n) :
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  else :
    f1 = 0
    f2 = 1
    for i in range(n) :
      inter = f2
      f2 = f1 + f2
      f1 = inter
    return f2

def sq(n) :
  return n * n

def cube(n) :
  return n * n * n

def pow2(n) :
  assert n >= 0
  res = 1
  for _ in range(n) :
    res *= 2
  return res

def odd(n) :
  return 2 * n + 1

def lin(a, b = 0) :
  return lambda x : a * x + b

def sqrt(n) :
  assert n >= 0
  root = 0
  sq_of_root = 0
  while sq_of_root <= n :
    sq_of_root += 2 * root + 1
    root += 1
  return root - 1

def adic(p, n) :
  res = 0
  while n % p == 0 :
    n /= p
    res += 1
  return res

def sum_adic(p, n) :
  sum = 0
  for i in range(1, n + 1) :
    sum += adic(p, i)
  return sum

##########################################
# main

u = lambda x : sum_adic(2, x)
n = 500

#for i in range(n + 1) :
# print(sq_rich_of(u, i))

#sq_rich_study(0, n, u)

for i in range(n + 1) :
  print(u(i))




#%prun( study_of_sq_rich(50) )
#sq_rich(4)
#00101001000100100010000100010000100000100001000001

