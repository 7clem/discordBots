#!/usr/bin/env python3
import sys
import math

def listeNombres(s):
    mots = s.split()
    nombres = []
    for m in mots:
        try:
            n = int(m.strip('.,!?'))
            nombres.append(n)
        except:
            pass
    print(nombres)
    return nombres

def contient(chaine, sub):
    if type(sub) == str:
        return chaine.find(sub) != -1
    else:
        for s in sub:
            if chaine.find(s) != -1:
                return True
        return False

class DevineModel:
    def __init__(self, bas=1, haut=100, essai=None):
        if bas != None and haut != None:
            self.intervale = [bas, haut]
            self.intervale.sort()
        if essai != None:
            self.essai = essai
        else:
            self.essai = math.floor(sum([bas, haut]) / 2)
        print(self)

    def divise(self):
        self.essai = math.floor(sum(self.intervale) / 2)

    def tropHaut(self):
        self.intervale = [self.intervale[0], self.essai]

    def tropBas(self):
        self.intervale = [self.essai, self.intervale[1]]

    def lireIntervale(self, s):
        self.joue = True
        nbs = listeNombres(s)
        if len(nbs) == 2:
            self.intervale = nbs
            self.joue = True
            self.divise()

    def __str__(self):
        i = str(self.intervale)
        e = str(self.essai)
        return f"DevineJoueur intervale={i}, essai={e}"

    def horsJeu(self):
        iv = self.intervale
        return iv == None or not isinstance(iv, list) or len(iv) != 2 or iv[0] > iv[1]

    def repond(self, cont:str):
        cont = cont.lower().strip(',. \n')
        if self.horsJeu():
            self.lireIntervale(cont)
        elif contient(cont,"gagné") or contient(cont, "trouvé"):
            self.intervale = []
            return "Belle partie. Merci."
        else:
            if cont.isnumeric():
                self.essai = int(cont)
                if self.essai > self.intervale[0]:
                    self.intervale[0] = essai
                if self.essai > intervale[1]:
                    self.intervale[1] = self.essai
                self.divise()
            elif contient(cont, ["haut", "élévé"]) or cont == 'h':
                self.tropHaut()
            elif contient(cont, ["bas", "petit"]) or cont == 'b':
                self.tropBas()
            self.divise()
        return str(self.essai)

if __name__ == "__main__":
    dm = DevineModel()
    for line in sys.stdin:
        reponse = dm.repond(line)
        print(reponse)
