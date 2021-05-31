#!/usr/bin/env python3

from statemachine import StateMachine, State

class BotStateMachine(StateMachine):
    # états
    repos = State('Repos', initial=True)
    choix = State('Choix')
    cherche = State('Cherche')

    # transition d'états
    lancer = repos.to(choix)
    choisir = choix.to(cherche)
    gagner = cherche.to(repos)

    def on_lancer(self):
        self.model.

if __name__ == "__main__":
    # object
    botState = BotStateMachine()

    print(botState.current_state)
    botState.current_state == BotStateMachine.attente == botState.attente
    print("botState.is_attente", botState.is_attente)
    print("botState.is_choix", botState.is_choix)
    print(" états : ",[s.identifier for s in botState.states])
    print(" transitions :", [t.identifier for t in botState.transitions])
