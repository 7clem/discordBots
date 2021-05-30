#!/usr/bin/env python3

from statemachine import StateMachine, State

class BotStateMachine(StateMachine):
    # états
    attente = State('Attente', initial=True)
    choix = State('Choix')
    devine = State('Devine')

    # transition d'états
    choisir = attente.to(choix)
    deviner = choix.to(devine)
    quitter = devine.to(attente)

# object
botState = BotStateMachine()

print(botState.current_state)
botState.current_state == BotStateMachine.attente == botState.attente
print("botState.is_attente", botState.is_attente)
print("botState.is_choix", botState.is_choix)
print(" états : ",[s.identifier for s in botState.states])
print(" transitions :", [t.identifier for t in botState.transitions])
