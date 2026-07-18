from collections import deque

PENALTY = {"J": 1, "Q": 2, "K": 3, "A": 4}
def simulate_game(player_a, player_b):
    deck_a = deque(player_a)
    deck_b = deque(player_b)
    pile = []
    cards_played = 0
    tricks = 0
    seen_states = set()
    turn = "a"
    
    while True: # OUTER
        def normalize(deck):
            return tuple('#' if card not in PENALTY else card for card in deck)
        
        state = (normalize(deck_a), normalize(deck_b), turn)
        if state in seen_states:
            return {"status": "loop", "cards": cards_played, "tricks": tricks}
        seen_states.add(state)
        
        current = turn
        owed = 0
        setter = None

        while True:  # INNER 
            current_deck = deck_a if current == "a" else deck_b
            if not current_deck:
                winner = "b" if current == "a" else "a"
                winner_deck = deck_a if winner == "a" else deck_b
                winner_deck.extend(pile)
                pile.clear()
                tricks += 1
                turn = winner
                loser_deck = deck_b if winner == "a" else deck_a
                if len(loser_deck) == 0:
                    return {"status": "finished", "cards": cards_played, "tricks": tricks}
                break

            card = current_deck.popleft()
            pile.append(card)
            cards_played += 1

            if card in PENALTY:
                setter = current
                payer = "b" if current == "a" else "a"
                owed = PENALTY[card]
                current = payer
            else:
                if owed == 0:
                    current = "b" if current == "a" else "a"
                else:
                    owed -= 1
                    if owed == 0:
                        winner_deck = deck_a if setter == "a" else deck_b
                        winner_deck.extend(pile)
                        pile.clear()
                        tricks += 1
                        turn = setter
                        loser_deck = deck_b if setter == "a" else deck_a
                        if len(loser_deck) == 0:
                            return {"status": "finished", "cards": cards_played, "tricks": tricks}                     
                        break   