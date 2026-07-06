from collections import Counter
RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
         '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def score_hand(cards):
    
    suits = [card[1] for card in cards]
    ranks = sorted([card[0] for card in cards], reverse=True)

    
    
    if set(ranks) == {14, 5, 4, 3, 2}:
        is_straight = True
        effective_ranks = [5, 4, 3, 2, 1]  
    else:
        is_straight = (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
        effective_ranks = ranks
    
        

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)
    tiebreak = sorted(ranks, key=lambda r: (rank_counts[r], r), reverse=True)
    
    is_flush = len(set(suits)) == 1
    is_full_house = counts == [3, 2]
    is_four_of_a_kind = counts == [4, 1]
    is_three_of_a_kind = counts == [3,1,1]
    is_two_pair = counts == [2,2,1]
    is_one_pair = counts == [2,1,1,1]
    
    
    if is_straight and is_flush:
        return (9, effective_ranks)
    elif is_four_of_a_kind:
        return (8, tiebreak)
    elif is_full_house:
        return (7, tiebreak)
    elif is_flush:
        return (6, ranks)
    elif is_straight:
        return (5, effective_ranks)
    elif is_three_of_a_kind:
        return (4, tiebreak)
    elif is_two_pair:
        return (3, tiebreak)
    elif is_one_pair:
        return (2, tiebreak)
    else:
        return (1, ranks)


    

def best_hands(hands):
    scored = []
    for hand in hands:
        cards = parse_hand(hand)
        score = score_hand(cards)
        scored.append((score, hand))
    
    best = max(scored, key=lambda x: x[0])
    return [hand for score, hand in scored if score == best[0]]


    
def parse_hand(hand):
    cards = []
    for card in hand.split(" "):
        suit = card[-1]
        rank = card[:-1]
        rank_value = RANKS[rank]
        cards.append((rank_value, suit))
    return cards
    
    
