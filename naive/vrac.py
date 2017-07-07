import naive as naive
import naive_occ as naive_occ


def thue_morse(n) :
  w = "0"
  k = n
  for k in range(n, 0, -1) :
    w2 = ""
    for c in w :
      if c == '0' :
        w2 += "01"
      else :
        w2 += "10"
    w = w2
  return w

#print(thue_morse(3))
#print(thue_morse(10))



##########################################
#tests (naive)

#w1 = input("word : ")
#squares_info(w1)


def print_squares_of(word) :
  print("Squares of " + word + " :")
  print(naive.squares_set(word))

def print_squares_of_input() :
  word = input("word : ")
  print(naive.squares_set(word))

"""
print_squares_of("abaabaa")
print_squares_of("aaabaaaba")
#print_squares_of("abababababababababababababaaaababababababbababbbbbaa")
print_squares_of("baababaababbbabbabbbab")
print_squares_of("0110100110010110100101100110100110010110011010010110100110010110")
"""

##########################################
#tests (naive_occ)

#naive_occ.squares_info(input("word : "))
#print(naive_occ.squares_inventory(input("word : ")))

def sq_rich(n) :
  s = ""
  bloc0 = "0"
  for _ in range(n) :
    s += bloc0 + "01" + bloc0 + "1" + bloc0 + "01"
    bloc0 += "0"
  return s

def study_of_sq_rich(n, m) :
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

%prun( study_of_sq_rich(50) )
#for i in range(20) :
#  print(sq_rich(i))   
    

#sq_rich(4)
#00101001000100100010000100010000100000100001000001

