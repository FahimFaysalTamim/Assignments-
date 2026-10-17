import math  #*************************** without mod

import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility(maxV, minV):
    return strength(maxV) - strength(minV) + (-1) ** random.randint(0, 1) * (random.randint(1, 10) / 10)

def minimax_without_mind_control(maxV, minV):
    return utility(maxV, minV)

def minimax_with_mind_control(maxV, minV):
    return max(utility(maxV, minV), utility(maxV, minV))

def main():
    first_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
    mind_control_cost = float(input("Enter the cost of using Mind Control: "))
    light_strength = float(input("Enter base strength for Light: "))
    l_strength = float(input("Enter base strength for L: "))
    
    if first_player == 0:
        maxV, minV = light_strength, l_strength
    else:
        maxV, minV = l_strength, light_strength
    
    no_mind_control = minimax_without_mind_control(maxV, minV)
    with_mind_control = minimax_with_mind_control(maxV, minV)
    final_mind_control = with_mind_control - mind_control_cost
    
    print(f"Minimax value without Mind Control: {no_mind_control:.2f}")
    print(f"Minimax value with Mind Control: {with_mind_control:.2f}")
    print(f"Minimax value with Mind Control after incurring the cost: {final_mind_control:.2f}")
    
    if final_mind_control > no_mind_control:
        print("Light should use Mind Control.")
    else:
        print("Light should NOT use Mind Control.")

main()
