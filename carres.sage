def squares(word):
    L = word.length()
    if L < 2:
        return []
    Sq = set()
    for i in range(0, L-1):
        for j in range(i+2, L+1, 2):
            fact = word[i:j]
            if fact.is_square():
                Sq.add(fact)
    return Sq

def longest_square_prefix(word):
    L = word.length()
    l = L % 2
    for i in range(L - l, 0, -2):
        if word[:i].is_square():
            return word[:i]
    return false

def longest_square_suffix(word):
    L = word.length()
    l = L % 2
    for i in range(l, L, 2):
        if word[i:].is_square():
            return word[i:]
    return false

def count_squares_in_prefix(word, max_length, nom_de_fichier):
    fichier = open(nom_de_fichier, 'w')
    for i in range(0, max_length/10 + 1):
        fichier.write(str(i*10))
        for j in range(10):
            fichier.write(" & ")
            fichier.write(str(len(squares(word[:10 * i + j]))))
        fichier.write(" \\\ \n")
    fichier.close() 

# Pour detecter les carres de longueur n dans un mot
def square_factor(word, n):
    # word must be finite, n is the length of the factors
    A = []
    for u in word.factor_set(n):
        if u.is_square():
            A.append(u)
    return A

def square_suffixes(word):
    l = word.length()
    suff = []
    for i in range(l-2, -1, -2):
        if word[i:].is_square():
            suff.append(word[i:])
    return suff        

# Enumerer les mots de longueur n qui contiennent deux suffixes carres unioccurrents
def enum_deux_suffixes(k, n):  # k est la taille de l'alphabet, n la longueur
    for w in Words(k,n):
        suff = set(square_suffixes(w))
        if len(suff) >= 2:
            uniocc = suff.difference(squares(w[:-1]))
            if len(uniocc) >= 2:
                print len(w), w, uniocc, len(squares(w))

def ensemble_suff_multiples(k, n):  # longueur n
    suffixes_m = set()
    for w in Words(k,n):
        suff = set(square_suffixes(w))
        if len(suff) >= 2:
            uniocc = tuple(suff.difference(squares(w[:-1])))
            if len(uniocc) >= 2:
                suffixes_m.add(uniocc)
    return suffixes_m

def ensemble_suff_multiples_et_longueur(k, n):  # longueur n
    suffixes_m = set()
    for w in Words(k,n):
        suff = set(square_suffixes(w))
        if len(suff) >= 2:
            uniocc = tuple(suff.difference(squares(w[:-1])))
            if len(uniocc) >= 2:
                suffixes_m.add(uniocc)
    suffixes_m_et_long = []
    for tup in suffixes_m:
        suffixes_m_et_long.append((tup[0], tup[0].length(), tup[1], tup[1].length()))
    return suffixes_m_et_long

#pour obtenir le nombre maximal de carres dans un mot de longueur n
def max_carres_deux_suffixes(k, n):  # k est la taille de l'alphabet, n la longueur
    max = 0
    for w in Words(k,n):
        suff = set(square_suffixes(w))
        if len(suff) >= 2:
            uniocc = suff.difference(squares(w[:-1]))
            if len(uniocc) >= 2:
                l = len(squares(w))
                if l > max:
                    max = l
    return max

