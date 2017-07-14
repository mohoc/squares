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

def test(a, b = 0, c = -1) :
  return "OK"

"""
print(test(2))
print(test(2,3))
print(test(2,3,4))
"""



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


