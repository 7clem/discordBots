#!/usr/bin/env python3

import discord
import random
import sqlite3
import sys

waiting = None
devine = None
devine_diff = None
devine_accept = None

## state pattern / Motif état
class DiscordBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.transitionTo(DevineWaiting(self))

    def transitionTo(self, state):
        self.state = state

    async def on_message(self, msg):
        # delegate to current state
        await self.state.on_message(msg)

class BotAbstractState:
    name = "BotAbstractState"
    allowed = []

    def __init__(self, context):
        self.context = context

    def switch(self, state):
        if state.name in self.allowed:
            print ('Current:', self, ' -> switched to new state:', state.name)
            self.__class__ = state
        else:
            print ('Current:',self, ' -> switching to ', state.name, ' not possible.')

    def __str__(self):
        return state.name

    async def on_message(self, message):
        raise NotImplementedError("This is an abstract base class. on_message()")

class Devine(BotAbstractState):
    def __init__(self, context:discord.Client):
        super().__init__(context)

    async def on_message(self, msg):
         print(Jeu Devine actif)

class DevineJeuEnCours(Devine):
    def __init__(self, context:discord.Client, difficult):
        super().__init__(context)
        self.nombre = random.randint(1, difficult)

    async def on_message(self, msg):
        with int(msg) as i:
            if i < self.nombre:
                await msg.channel.send("Trop petit")

class DevineDifficulte(Devine):
    difficultes = [10, 100, 1000]

    def __init__(self, context:discord.Client):
        super().__init__(context)

    async def on_message(self, msg):
        possibilities = [str(x) for x in difficultes]
        print(possibilities)
        if msg.content in possibilities:
            nb = int(msg.content)
            self.context.transitionTo(DevineJeuEnCours(self.context, nb))
            await msg.channel.send(f"Ok. J'ai un nombre entre 1 et {nb}. Devine-le")
        else:
            await msg.channel.send(f"On attend ici un nombre parmi {possibilities}")


class DevineWaiting(Devine):
    name = 'Waiting'
    allowed = ['Devine']

    async def on_message(msg):
        if msg.content.lower() == "devine":
            await msg.channel.send("Ok, jouons à Devine-le-nombre !")
            self.context.transitionTo(DevineDifficulte(self.context))
        elif msg.content.lower() in ['h', 'help', 'aide', 'commandes']:
            await msg.channel.send("devine -> demarre le jeu 'Devine-Le-nombre'")


def usage():
    return """
    pfc -> joue à pierre feuille ciseaux.
    devine mon nombre -> le bot va trouver ton nombre
    pense à un nombre -> le bot va
    joue -> démarre une partie
    stop -> arrète la partie
    score -> compte les points
    """



# @client.event
# async def on_message(msg):
#     if not state:
#
#     if msg.content == "pfc":
#         await msg.channel.send("C'est mon nom.")
#     elif msg.content == "joue":
#         await msg.channel.send("prêt ? 3...")
#     elif msg.content == "aide" or msg.content == "help" or msg.content == 'h':
#         await msg.channel.send(usage())
#     elif msg.content == "devine le nombre":
#         state = DevineLeNombre()

if __name__ == "__main__":
    bot = DiscordBot()
    discordBotToken = ""
    with open(sys.argv[1]) as dbtFile:
        discordBotToken = dbtFile.readlines()[0]
    print("Discord Bot running")
    bot.run(discordBotToken)

    state = None
