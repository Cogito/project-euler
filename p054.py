from collections import Counter


def p054():
    wins = 0
    with open("p054_poker.txt") as hands:
        for hand in hands:
            hand = hand.split()
            player1 = [text_to_card(c) for c in hand[:5]]
            player2 = [text_to_card(c) for c in hand[5:]]
            if score(player1) > score(player2):
                wins += 1
    print(wins)


def score(hand):
    s = 0
    # highest card first points
    s += sum(10 ** (2 * n) * value for n, value in enumerate(sorted(value for value, _ in hand)))
    # count pairs, three of a kind, four of a kind
    multiples = Counter((value for value, _ in hand))
    pairs = sorted(value for value, count in multiples.items() if count == 2)
    threes = [value for value, count in multiples.items() if count == 3]
    fours = [value for value, count in multiples.items() if count == 4]
    if len(pairs) >= 1:  # first pair
        s += 10 ** (2 * 5) * pairs[0]
    if len(pairs) == 2:  # second pair
        s += 10 ** (2 * 6) * pairs[1]
    if len(threes) == 1:  # three of a kind
        s += 10 ** (2 * 7) * threes[0]
    if is_straight(hand):
        s += 10 ** (2 * 8)
    if is_flush(hand):
        s += 10 ** (2 * 9)
    if len(threes) == 1 and len(pairs) == 1:  # full house
        s += 10 ** (2 * 10)
    if len(fours) == 1:  # four of a kind
        s += 10 ** (2 * 11) * fours[0]
    if is_straight(hand) and is_flush(hand):
        s += 10 ** (2 * 12)
    return s


def is_straight(hand):
    values = sorted(value for value, _ in hand)
    return values == list(range(values[0], values[0] + 5))


def is_flush(hand):
    suits = sorted(suit for _, suit in hand)
    return suits == 5 * [suits[0]]


def text_to_card(c):
    value, suit = c
    face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    card_values = {**face_cards, **dict((str(n), n) for n in range(2, 10))}
    value = card_values.get(value)
    return value, suit


def test_p054():
    assert text_to_card('8C') == (8, 'C')
    assert text_to_card('AC') == (14, 'C')
    assert (1, 2, 3) < (2, 1, 1)
    assert sorted((1, 2, 3), reverse=True) > sorted((2, 2, 2), reverse=True)
    assert is_straight([text_to_card(c) for c in '2C 3C 4C 5C 6C'.split()])
    assert is_flush([text_to_card(c) for c in '2C 3C 4C 5C 6C'.split()])


if __name__ == '__main__':
    p054()
