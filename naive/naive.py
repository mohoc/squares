"""
A naive algorithm to find the distinct squares in a finite word.
Especially it only takes into account the last occurence and
its ending position.

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

#type word = string.

def is_square(word, beg_pos, end_pos) :
  candidate_len = end_pos - beg_pos + 1
  if candidate_len % 2 == 1 :
    return False
  else :
    mid_len = candidate_len // 2
    return word[beg_pos : beg_pos + mid_len] == word[beg_pos + mid_len : end_pos + 1]

def squares_set(word) :
  squares_set = set()
  n = len(word)
  for end_pos in range(n) :
    for beg_pos in range(end_pos + 1) :
      if is_square(word, beg_pos, end_pos) :
        squares_set.add(word[beg_pos : end_pos + 1])
  return squares_set

def squares_inventory(word) :
  squares_positions = {}
  n = len(word)
  for end_pos in range(n - 1, -1, -1) :
    for beg_pos in range(end_pos, -1, -1) :
      if is_square(word, beg_pos, end_pos) :
        mid_length = (end_pos - beg_pos + 1) // 2
        squares_positions[word[beg_pos : beg_pos + mid_length]] = end_pos + 1
  #empty word
  squares_positions[""] = 0
  return squares_positions

def squares_distribution(sq_inventory, len_word) :
  nb_squares_at_pos = [0 for _ in range(len_word + 1)]
  for square in sq_inventory :
    nb_squares_at_pos[sq_inventory[square]] += 1
  return nb_squares_at_pos

#l for lacunar, s for simple, d for double
def print_squares_distribution(sq_distrib, characters = ('l', 's', 'd')) :
  d = len(sq_distrib)
  for pos in range(d) :
    print(characters[sq_distrib[pos]], end = "")
  print("")

def print_squares_distribution_with_word(word, sq_distrib, characters = ('l', 's', 'd')) :
  d = len(sq_distrib)
  assert d == len(word) + 1
  print(characters[sq_distrib[0]], end = "")
  for pos in range(1, d) :
    print(word[pos - 1], end = "")
    print(characters[sq_distrib[pos]], end = "")
  print("")

def positions_with_nb_squares(word, i) :
  n = len(word)
  sq_distrib = squares_distribution(squares_inventory(word), n)
  pos_wanted = []
  for pos in range(n) :
    if sq_distrib[pos] == i :
      pos_wanted.append(pos)
  return pos_wanted

def lacunas(word) :
  return positions_with_nb_squares(word, 0)

def double_squares(word) :
  return positions_with_nb_squares(word, 2)

def squares_info(word) :
  n = len(word)
  sq_inventory = squares_inventory(word)
  squares_positions = list(sq_inventory.items())
  squares_positions.sort(key=lambda tup: tup[1])
  nb_squares = len(squares_positions)
  defect = n - nb_squares + 1
  sq_distrib = squares_distribution(sq_inventory, n)
  print("")
  print("### word length : {}".format(n))
  print("### number of squares : {}".format(nb_squares))
  print("### square defect : {}".format(defect))
  print("### square distribution :")
  print_squares_distribution_with_word(word, sq_distrib, ('_', '-', '*'))
  if not input("print the square factors ? [Y/n] : ") in ["n", "N", "no", "No"]:
    print("### squares :")
    for square, first_pos in squares_positions :
      print("{}\t{}".format(first_pos, square))

def nb_squares(word) :
  return len(squares_inventory(word))

def defect(word) :
  return len(word) - nb_squares(word) + 1

