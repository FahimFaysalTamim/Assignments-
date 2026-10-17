

#Problem 1


import math
import random

def calculation(x):
    return math.log2(x + 1) + (x / 10)

def value(maxV, minV):
    i = random.choice([0, 1])
    return round(strength(maxV) - strength(minV) + ((-1) ** i * random.randint(1, 10) / 10), 2)

def minmax(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0:
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = minmax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = minmax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def game(starting_player, carlsen_strength, caruana_strength):
    results = []
    max_wins = 0
    min_wins = 0
    draws = 0

    for game in range(4):
        maxV = carlsen_strength if (game % 2 == starting_player) else caruana_strength
        minV = caruana_strength if (game % 2 == starting_player) else carlsen_strength

        values = [utility(maxV, minV) for _ in range(2 ** 5)]
        result = minmax(5, 0, True, values, float('-inf'), float('inf'))
        results.append(result)

        if result > 0:
            max_wins += 1
            winner = "Magnus Carlsen" if maxV == carlsen_strength else "Fabiano Caruana"
        elif result < 0:
            min_wins += 1
            winner = "Magnus Carlsen" if minV == carlsen_strength else "Fabiano Caruana"
        else:
            draws += 1
            winner = "Draw"

        print(f"Game {game + 1} Winner: {winner} (Utility value: {result})")

    print("\nOverall Results:")
    print(f"Magnus Carlsen Wins: {max_wins if starting_player == 0 else min_wins}")
    print(f"Fabiano Caruana Wins: {min_wins if starting_player == 0 else max_wins}")
    print(f"Draws: {draws}")

    if max_wins > min_wins:
        print("Overall Winner: Magnus Carlsen")
    elif min_wins > max_wins:
        print("Overall Winner: Fabiano Caruana")
    else:
        print("Overall Winner: Draw")

starting_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
carlsen_strength = float(input("Enter base strength for Carlsen: "))
caruana_strength = float(input("Enter base strength for Caruana: "))

play_game(starting_player, carlsen_strength, caruana_strength)



