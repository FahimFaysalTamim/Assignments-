import math
import random

def calculate_power(value):
    """Calculate the power based on the input value."""
    return math.log2(value + 1) + (value / 10)

def evaluate_move(max_value, min_value):
    """Evaluate the move based on the maximum and minimum values, 
    with a small random fluctuation to simulate uncertainty."""
    return calculate_power(max_value) - calculate_power(min_value) + (-1) ** random.randint(0, 1) * (random.randint(1, 10) / 10)

def basic_strategy(max_value, min_value):
    """Basic strategy without any special abilities like mind control."""
    return evaluate_move(max_value, min_value)

def enhanced_strategy(max_value, min_value):
    """Enhanced strategy that uses the mind control effect (without any cost adjustment)."""
    return max(evaluate_move(max_value, min_value), evaluate_move(max_value, min_value))

def game_decision():
    """Main function to run the game and decide if Mind Control should be used."""
    starting_player = int(input("Who goes first? (0 for Light, 1 for L): "))
    mind_control_cost = float(input("Enter the cost of using Mind Control: "))
    light_power = float(input("Enter Light's base power: "))
    l_power = float(input("Enter L's base power: "))
    
    if starting_player == 0:
        max_value, min_value = light_power, l_power
    else:
        max_value, min_value = l_power, light_power
    
    basic_strategy_value = basic_strategy(max_value, min_value)
    enhanced_strategy_value = enhanced_strategy(max_value, min_value)
    final_value_with_cost = enhanced_strategy_value - mind_control_cost
    
    print(f"Basic strategy value: {basic_strategy_value:.2f}")
    print(f"Enhanced strategy value (without cost): {enhanced_strategy_value:.2f}")
    print(f"Enhanced strategy value after cost: {final_value_with_cost:.2f}")
    
    if final_value_with_cost > basic_strategy_value:
        print("Mind Control should be used.")
    else:
        print("Mind Control should NOT be used.")

game_decision()
