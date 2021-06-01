#!/usr/bin/env python3

import discord
import random
import sqlite3
import sys
import math
from devinemodel import DevineModel
#from botStateMachine import BotStateMachine


class DevineJoueur(discord.Client):
    def __init__(self):
        super().__init__()
        self.intervale = []
        self.essai = 0
        self.joue = False
        self.model = DevineModel()

    async def on_ready(self):
        print("Le bot discord est actif.")

    async def on_message(self, msg):
        if (msg.author == self.user):
            return

        s = self.model.repond(msg.content)
        await msg.channel.send(s)


def discordBotToken():
    discordBotToken = ""
    with open(sys.argv[1]) as dbtFile:
        return dbtFile.readlines()[0]


if __name__ == "__main__":
    bot = DevineJoueur()
    #etat = BotStateMachine(bot)

    bot.run(discordBotToken())
