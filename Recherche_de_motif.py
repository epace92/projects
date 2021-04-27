def brutForce(T, M):
    """
    Algorithme permettant de retrouver la position du motif recherché M dans un texte T
    :param T: string, texte quelconque
    :param M: string, le motif recherché dans le texte
    :return: int, la position de la premiere lettre du motif dans le texte T
    """
    for i in range(len(T)-len(M)):
        if M == T[i:i+len(M)]:
            return i
    return -1

def boyer_moore(T, M):
    """
    Algorithme moins couteux que le premier qui recherche un motif M dans un texte T
    :param T: strkng, un texte quelconque
    :param M: string, le motif recherché
    :return: 1 si le motif est dans le texte, -1 sinon (dans le cas ---> retourne aussi la position de la premiere
    lettre du motif
    """
    i = 0
    while i <= len(T)-len(M):
        update = i
        if i == len(T)-len(M) and M[-1] != T[-1]:
            return -1
        temp = 0
        j = -1
        OK = True
        while j > -len(M)-1 and OK is not False:
            k = i+len(M)-1-temp
            if M[j] != T[k]:
                i = saut(T, M, i, k)
                OK = False
            temp += 1
            j -= 1
        if update == i:
            return 1, i

# saut(m-i-1)
# m: taille du mot
# i: valeur de la lettre dans le dictionnaire du motif
def saut(T, M, i, k):
    """
    Retourne la nouvelle position initiale dans la chaine de caractere T pour commencer a comparer au motif M
    :param T: string, texte quelconque
    :param M: string, le motif recherche
    :param i: int, la position actuelle
    :param k: int, la position de la derniere lettre comparee
    :return: int, la nouvelle position etudiee
    """
    A = construit_alphabet(T)
    L = traiter_motif(A, M)
    if L[T[k]] != -1:
        i += (len(M) - L[T[k]] - 1)
        return i
    else:
        i += len(M)
        return i

def traiter_motif(A, M):
    """
    Retourne un dictionnaire des lettres du motif ainsi que de la position de leur dernière occurence
    Toutes les lettres de l'alphabet sont référencés et la valeur -1 leur est attribuée si cette dernière n'est pas
    présente dans le motif M
    :param A: list, l'alphabet
    :param M: string, le motif recherché
    :return: dict
    """
    L = {}
    for i in range(len(M)):
        L[M[i]] = i
    for k in range(len(A)):
        if A[k] not in L.keys():
            L[A[k]] = -1
    return L

def construit_alphabet(T):
    """
    Construit une liste contenant toutes les lettres contenues dans un texte T en tenant compte des occurences
    :param T: un texte quelconque
    :return: list, contenant une seule fois chaque lettre de T
    """
    A = []
    for i in range(len(T)):
        if T[i] not in A and ord(T[i]) != 32:
            A.append(T[i])
    return A

#=======================================================================#
#                               TESTS                                   #
#=======================================================================#
print("brutForce(\"Je vais en vacances\", \"ais\"):", brutForce("Je vais en vacances", "ais"))
print("traiter_motif(\"stupid spring string\", \"string\"):", traiter_motif("stupid spring string", "string"))
print(traiter_motif("stupid spring string", "string").keys())
print("construit_alphabet(\"stupid spring string\"):", construit_alphabet("stupid spring string"))
print("boyer_moore(\"stupid spring string\", \"string\"):", boyer_moore("stupid spring string", "string"))