"""
Provides information about square factors in a given finite word
with naive algorithms.
Including :
- the number of distinct squares
- the total number of squares
- the square defect
- the list of the square factors and their positions
- the distribution of squares among the positions of the word
"""


import naive as naive
import naive_occ as naive_occ

with_occ_answer = input("study with all the occurences ? [y/N] : ")
if with_occ_answer in ["y", "Y", "yes", "Yes"]:
  with_occ = True
  with_end_pos_answer = input("with end positions / middle positions ? [E/m] : ")
  with_end_pos = not with_end_pos_answer in ["m", "M"]
else :
  with_occ = False

w1 = input("word : ")
if with_occ :
  naive_occ.squares_info(w1, with_end_pos)
else :
  naive.squares_info(w1)




