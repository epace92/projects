class Item:
    def __init__(self, indObj, weight, value):
        """
        Initialise un objet de classe Item avec ses attributs indObjet, weight, value et ratio
        :param indObj: int, permet d'identifier l'objet par un numéro
        :param weight: int, le poids de l'objet en question
        :param value: int, la valeur que l'objet represente
        """
        self.indObj = indObj
        self.weight = weight
        self.value = value
        self.ratio = value/weight

    def __str__(self):
        """
        Retourne une representation de l'instance de la classe Item
        :return: string
        """
        return str(self.indObj) + ":(" + str(self.weight) + "," + str(self.value) + ")"

    def __lt__(self, other):
        """
        Retourne True si self est strictement inferieur a other (on compare les ratios)
        :param other: une instance de la classe Item
        :return: bool
        """
        return self.ratio < other.ratio

    def __gt__(self, other):
        """
        Retourne True si self est strictement superieur a other (on compare les ratios)
        :param other: une instance de la classe Item
        :return: bool
        """
        return self.ratio > other.ratio

    def __eq__(self, other):
        """
        Retourne True si self est egal a other (on compare les ratios)
        :param other: une instance de la classe Item
        :return: bool
        """
        return self.ratio == other.ratio

class SAD:
    def __init__(self, itemsSac, capacity, nitem):
        """
        Initialise un objet de la classe SAD
        :param itemsSac: dict, contient les differents objets a mettre dans le sac
        :param capacity: int, la capacite maximale de l'objet SAD
        :param nitem: int, le nombre d'objet dans l'objet SAD
        """
        self.itemsSac = itemsSac
        self.capacity = capacity
        self.nitem = nitem

    def __str__(self):
        """
        Retourne une representation sous forme de string de l'instance de classe SAD
        :return: string, une representation
        """
        ans = "{"
        cpt = 0
        for k in self.itemsSac.keys():
            cpt += 1
            if cpt == self.nitem:
                ans += str(self.itemsSac[k]) + "}"
            else:
                ans += str(self.itemsSac[k]) + " ; "
        return ans

    def add_to_sac(self, i, w, v):
        """
        Ajoute un objet au dictionnaire self.itemsSac
        :param i: int, identifiant de l'objet
        :param w: int, poids de l'objet
        :param v: int, valeur de l'objet
        """
        self.itemsSac[i] = Item(i, w, v)
        self.nitem += 1

    def build_sorted_list(self):
        """
        Trie la liste des Items dans l'ordre decroissant de leur ratio
        :return: list
        """
        l = list(self.itemsSac.values())
        l.sort(reverse=True)
        return l

    def get_value_max(self):
        """
        Retourne la valeur maximale des objets que l'on peut mettre dans le sac en fonction de la capacité du sac
        et des poids des différents objets
        :return: le poids du sac et sa valeur
        """
        stock = self.capacity
        val = 0
        l = self.build_sorted_list()
        i = 0
        while i < len(l):
            if l[i].weight <= stock:
                val += (stock//l[i].weight)*l[i].value
                stock -= (stock//l[i].weight)*l[i].weight
            i += 1
        return "weight : " + str(self.capacity-stock) + ", value : " + str(val)

    # =======================================================================#
    #                               TESTS                                    #
    # =======================================================================#
obj1 = Item(1, 2, 6)
print("obj1 --->", obj1)
d = {}
sad = SAD(d, 15, 0)
sad.add_to_sac(1, 2, 6)
sad.add_to_sac(2, 1, 1)
sad.add_to_sac(3, 5, 18)
sad.add_to_sac(4, 6, 22)
sad.add_to_sac(5, 7, 24)
print("sad --->", sad)
sad.build_sorted_list()
string = "{"
cpt = 0
for var in sad.build_sorted_list():
    cpt += 1
    if cpt == len(sad.build_sorted_list()):
        string += str(var) + "}"
    else:
        string += str(var) + " ; "
print("sad.build_sorted_list() --->", string)
print("sad.get_value_max() --->", sad.get_value_max())