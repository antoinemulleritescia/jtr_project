import hashlib

class generateur:   # <<< CECI EST UNE CLASS, il faut bien la regarder et la savourer car c est la seul
# ^^ Au dessus, une class

    def __init__(self, listfinal):  #je fais des truc mais ¿¿¿
        self.listfinal=listfinal    #toi c est toi



    def convMaj(self):  #explicite
        listmaj = []
        for mot in self.listfinal:

            longueur = len(mot)
            npossi = 2 ** longueur - 1

            while npossi > -1:
                z = 0
                c = ""

                nbin = bin(npossi)
                nbin = nbin[2:]
                comparateur = str(nbin)

                if len(comparateur) < longueur:
                    ncaracadd = longueur - len(comparateur)
                    comparateur = comparateur.zfill(len(comparateur) + ncaracadd)
                for i in mot:
                    if comparateur[z] == "0":
                        c = c + i.upper()
                    else:
                        c = c + i
                    z = z + 1
                listmaj.append(c)
                npossi = npossi - 1

        self.listfinal = listmaj
        return self.listfinal

# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================

    def addCarac(self): #explicite
        listaddc = []

        for mot in self.listfinal:
            ca = "a"
            y = 0
            while y < 26:
                y = y + 1

                text = ca + mot
                listaddc.append(text)

                text = ca.upper() + mot
                listaddc.append(text)

                text = mot + ca
                listaddc.append(text)

                text = mot + ca.upper()
                listaddc.append(text)

                ca = chr(ord(ca) + 1)
        self.listfinal = listaddc
        return self.listfinal

# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================

    def chiffreAD(self, nbchiffre): #explicite
        listaddchif = []
        limite = 10 ** nbchiffre - 1

        for mot in self.listfinal:
            compteur = 0
            while compteur < limite:
                compteur = compteur + 1
                compteurdigit = str(compteur).zfill(nbchiffre)
                bonchiffre = compteurdigit[-4:]
                text = mot + str(bonchiffre)
                listaddchif.append(text)
                text = str(bonchiffre) + mot
                listaddchif.append(text)

        self.listfinal = listaddchif
        return self.listfinal

# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================

    def reversedouble(self): #explicite
        listreversedouble = []
        for mot in self.listfinal:

            reverse = ""
            longueur = len(mot)
            longueur -= 1

            while int(longueur) != -1:
                reverse += mot[int(longueur)]
                longueur -= 1
            double = reverse + reverse
            listreversedouble.append(double)

        self.listfinal = listreversedouble
        return self.listfinal

# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================

    def comboani(self): #explicite
        listcomboani = []
        for mot in self.listfinal:
            combo = mot
            for smot in self.listfinal:
                combofinal = combo + smot
                listcomboani.append(combofinal)
        self.listfinal = listcomboani
        return self.listfinal

# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================

    def voy(self): #explicite
        x = 0
        listvoy = []

        for mot in self.listfinal:
            while x < 10:
                mot = mot.upper()
                motfinal = (mot.replace("A", str(x)))
                motfinal = (motfinal.replace("E", str(x)))
                motfinal = (motfinal.replace("U", str(x)))
                motfinal = (motfinal.replace("I", str(x)))
                motfinal = (motfinal.replace("O", str(x)))
                motfinal = (motfinal.replace("Y", str(x)))
                x += 1
                listvoy.append(motfinal)
            x = 0
        self.listfinal = listvoy
        return self.listfinal

