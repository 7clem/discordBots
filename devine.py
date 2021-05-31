#!/usr/bin/env python3

import discord
import random
import sqlite3
import sys
import math
#from botStateMachine import BotStateMachine

def listeNombres(s):
    mots = s.split()
    print(mots)
    nombres = []
    for m in mots:
        try:
            n = int(m.strip('.,!?'))
            print("trouvé", n)
            nombres.append(n)
        except:
            pass
    return nombres

def contient(chaine, sub):
    if type(sub) == str:
        return chaine.find(sub) != -1
    else:
        for s in sub:
            if chaine.find(s) != -1:
                return True
        return False

class DevineJoueur(discord.Client):
    def __init__(self):
        super().__init__()
        self.intervale = []
        self.essai = 0
        self.joue = False

    async def on_ready(self):
        print("Le bot discord est actif.")

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

    async def on_message(self, msg):
        if (msg.author == self.user):
            return
        cont = msg.content.lower()
        print(cont)
        prefix = "Ok, j'ai choisi un nombre au hazard entre ".lower()
        if cont.startswith(prefix):
            self.lireIntervale(cont)
        elif contient(cont,"gagné") or contient(cont, "trouvé"):
            self.joue = False
            return
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
            await msg.channel.send(str(self.essai))



    def __str__(self):
        i = str(self.intervale)
        e = str(self.essai)
        j = str(self.joue)
        return f"DevineJoueur intervale={i}, essai={e}, joue={j}"

if __name__ == "__main__":
    bot = DevineJoueur()
    #etat = BotStateMachine(bot)
    discordBotToken = ""
    with open(sys.argv[1]) as dbtFile:
        discordBotToken = dbtFile.readlines()[0]

    bot.run(discordBotToken)
