import random

# Initial Configurations
initial_capital = 1000
historical_prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
population_size = 4
generations = 10

# Initial Population
population = [
    {"stop_loss": 2, "take_profit": 5, "trade_size": 20},
    {"stop_loss": 3, "take_profit": 7, "trade_size": 30},
    {"stop_loss": 1.5, "take_profit": 4, "trade_size": 25},
    {"stop_loss": 2.5, "take_profit": 6, "trade_size": 15},
]

# Fitness Function (Profit Calculation)
def evaluate_fitness(strategy):
    capital = initial_capital
    for change in historical_prices:
        trade_amount = (capital * strategy["trade_size"]) / 100

        if change <= -strategy["stop_loss"]:
            loss = trade_amount * (strategy["stop_loss"] / 100)
            capital -= loss
        elif change >= strategy["take_profit"]:
            profit = trade_amount * (strategy["take_profit"] / 100)
            capital += profit
        else:
            capital += (trade_amount * change) / 100

    return capital - initial_capital

# Selection (Pick best parents)
def select_parents(population):
    fitness_scores = [evaluate_fitness(ind) for ind in population]
    return random.choices(population, weights=fitness_scores, k=2)

# Crossover (Mix Parent Genes)
def crossover(parent1, parent2):
    child = {
        "stop_loss": (parent1["stop_loss"] + parent2["stop_loss"]) / 2,
        "take_profit": (parent1["take_profit"] + parent2["take_profit"]) / 2,
        "trade_size": (parent1["trade_size"] + parent2["trade_size"]) / 2,
    }
    return child

# Mutation (Small Random Changes)
def mutate(strategy):
    if random.random() < 0.2:  # 20% mutation chance
        strategy["stop_loss"] += random.uniform(-0.5, 0.5)
        strategy["take_profit"] += random.uniform(-0.5, 0.5)
        strategy["trade_size"] += random.uniform(-2, 2)
    return strategy

# Genetic Algorithm
for _ in range(generations):
    new_population = []
    for _ in range(population_size // 2):  # Half new, half old
        p1, p2 = select_parents(population)
        child = mutate(crossover(p1, p2))
        new_population.append(child)
    population = sorted(population + new_population, key=evaluate_fitness, reverse=True)[:population_size]

# Best Strategy
best_strategy = population[0]
final_profit = evaluate_fitness(best_strategy)

print("Best Strategy:", best_strategy)
print("Final Profit:", round(final_profit, 2))
