#!/usr/bin/env python3

import discord
import random
import sqlite3

waiting = None
devine = None
devine_diff = None
devine_accept = None

## state pattern / Motif état
class DiscordBot(discord.Client):
    def __init__(self, initialState):
        super().__init__()
        self.transitionTo(initialState)

    def transition(self, state):
        self.state = state

    def on_message(self, msg):
        # delegate to current state
        self.state.on_message(message)

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

    def on_message(self, message):
        raise NotImplementedError("This is an abstract base class.")

class DevineWaiting(Devine):
    name = 'Waiting'
    allowed = ['Devine']

    async def on_message(msg):
        if msg.content.lower() == "devine":
            await msg.channel.send("Ok, jouons à Devine-le-nombre !")
        else:
            await msg.channel.send("Les commandes sont : devine")

class Devine(BotAbstractState):
    def __init__(self, context:DiscordClient):
        super().__init__(context)

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
    bot = DiscordBot(DevineWaiting)
    discordBotToken = argv[1]
    bot.run(discordBotToken)
    state = None
