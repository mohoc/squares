"""
A naive algorithm to find the squares in a finite word and count their
occurences.

*Method used :
  check the square property on every factor.

*Complexity 
  (with n the word length and s the number of squares) :
    - nb checks : O(n**2)
    - a single check :
      - square-property checking : O(n)
      - add a square in the set of squares : O(n * log(s))
        (with efficient implementation of type set)

  All in all : O(n**3 * log(s))
"""

from naive import *

def is_square(word, beg_pos, end_pos) :
  candidate_len = end_pos - beg_pos + 1
  if candidate_len % 2 == 1 :
    return False
  else :
    mid_len = candidate_len // 2
    return word[beg_pos : beg_pos + mid_len] == word[beg_pos + mid_len : end_pos + 1]

def squares_inventory(word) :
  squares_positions = {}
  n = len(word)
  for end_pos in range(n) :
    for beg_pos in range(end_pos + 1) :
      if is_square(word, beg_pos, end_pos) :
        mid_length = (end_pos - beg_pos + 1) // 2
        square = word[beg_pos : beg_pos + mid_length]
        if square in squares_positions :
          squares_positions[square].append(end_pos + 1)
        else :
          squares_positions[square] = [end_pos + 1]
  #empty word
  squares_positions[""] = [0]
  return squares_positions

def squares_distribution_end(sq_inventory_occ, len_word) :
  nb_squares_at_pos = [0 for _ in range(len_word + 1)]
  for square in sq_inventory_occ :
    for pos in sq_inventory_occ[square] :
      nb_squares_at_pos[pos] += 1
  return nb_squares_at_pos

def squares_distribution_mid(sq_inventory_occ, len_word) :
  nb_squares_at_pos = [0 for _ in range(len_word + 1)]
  for square in sq_inventory_occ :
    len_sq = len(square)
    for pos in sq_inventory_occ[square] :
      nb_squares_at_pos[pos - len_sq]  += 1
  return nb_squares_at_pos

def print_squares_distribution(sq_distrib_occ) :
  n = len(sq_distrib_occ)
  for pos in range(n) :
    print("{} ".format(sq_distrib_occ[pos]), end = "")
  print("")

def squares_info(word, with_end_pos) :
  n = len(word)
  sq_inventory = squares_inventory(word)
  squares_positions = list(sq_inventory.items())
  squares_positions.sort(key=lambda tup: tup[1][0])
  nb_distinct_squares = len(squares_positions)
  if with_end_pos :
    sq_distrib = squares_distribution_end(sq_inventory, n)
    pos_chosen = "end"
  else :
    sq_distrib = squares_distribution_mid(sq_inventory, n)
    pos_chosen = "mid"
  nb_squares = sum(sq_distrib)
  print("")
  print("### word length : {}".format(n))
  print("### number of distinct squares : {}".format(nb_distinct_squares))
  print("### number of squares : {}".format(nb_squares))
  print("### square distribution ({}) :".format(pos_chosen))
  print_squares_distribution(sq_distrib)
  if not input("print the square factors ? [Y/n] : ") in ["n", "N", "no", "No"]:
    print("### squares :")
    for square, positions in squares_positions :
      nb_pos = len(positions)
      print("{}\t{}\t{}".format(square, nb_pos, positions[0]), end = "")
      for i in range(1, nb_pos) :
        print(",{}".format(positions[i]), end = "")
      print("")
    
    


