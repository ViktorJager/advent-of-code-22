# aoc day 2

def read_file(path):
    with open(path) as f:
        return f.readlines()

def filter_newline(str):
    return str.replace("\n", "")

def handify(str):
    chars = str.split()
    return (convert_hand(chars[0]), convert_hand(chars[1]))

def handify_pt2(str):
    chars = str.split()
    desired_outcome = chars[1]
    opponent_hand = chars[0]
    
    # win
    if desired_outcome == 'Z':
        if opponent_hand == 'A':
            return ('rock', 'paper')
            
        if opponent_hand == 'B':
            return ('paper', 'scissors')
        if opponent_hand == 'C':
            return ('scissors', 'rock')

    # draw
    if desired_outcome == 'Y':
        if opponent_hand == 'A':
            return ('rock', 'rock')
        if opponent_hand == 'B':
            return ('paper', 'paper')
        if opponent_hand == 'C':
            return ('scissors', 'scissors')

    # loose
    if desired_outcome == 'X':
        if opponent_hand == 'A':
            return ('rock', 'scissors')
        if opponent_hand == 'B':
            return ('paper', 'rock')
        if opponent_hand == 'C':
            return ('scissors', 'paper')

def convert_hand(str):
    if str in ('A', 'X'):
        return 'rock'
    if str in ('B', 'Y'):
        return 'paper'
    if str in ('C', 'Z'):
        return 'scissors'


def award_hand_points(choice):
    if choice == 'rock':
        return 1
    if choice == 'paper':
        return 2
    if choice == 'scissors':
        return 3

lines = read_file('./input/day2/input.txt')
filtered_lines = list(map(filter_newline, lines))
hands = list(map(handify_pt2, filtered_lines))


def rps(hand):
    player1 = hand[0]
    player2 = hand[1]

    hp = award_hand_points(player2)

    print(f"player1: {player1}, player2: {player2}")
    print(f"handpoints: +{hp}")

    if (player1 == "rock" and player2 == "paper") \
        or (player1 == "paper" and player2 == "scissors") \
        or (player1 == "paper" and player2 == "scissors") \
        or (player1 == "scissors" and player2 == "rock"):
            return hp + 6
    elif player1 == player2:
        return hp + 3
    else:
        return hp + 0


PLAYER_POINTS = 0
round = 1
for hand in hands:
    print(f"ROUND {round}")
    round_score = rps(hand)
    PLAYER_POINTS += round_score
    print(f"total round_score: +{round_score}")
    print(f"PLAYER_POINTS: {PLAYER_POINTS}")
    print("------")

    round += 1
