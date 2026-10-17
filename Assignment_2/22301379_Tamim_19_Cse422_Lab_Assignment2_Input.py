import random

def initialize_population(initial_population):
    return initial_population
    

def evaluate_fitness(chromosome, historical_prices, initial_capital=1000):
    capital = initial_capital
    #print(chromosome["stop_loss"])
    for price_change in historical_prices:
        trade_amount = capital * (chromosome["trade_size"] / 100)
        #print(trade_amount)
        
        if price_change <= -chromosome["stop_loss"]:
            profit_loss = -trade_amount * (chromosome["stop_loss"] / 100)
        elif price_change >= chromosome["take_profit"]:
            profit_loss = trade_amount * (chromosome["take_profit"] / 100)
        else:
            profit_loss = trade_amount * (price_change / 100)
        
        capital += profit_loss
    return capital - initial_capital

def select_parents(population, fitness_scores):
    return random.choices(population, weights=fitness_scores, k=2)

def crossover(parent1, parent2):
    crossover_point = random.choice(["stop_loss", "take_profit", "trade_size"])
    child = parent1.copy()
    child[crossover_point] = parent2[crossover_point]
    return child

def mutate(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        mutation_key = random.choice(["stop_loss", "take_profit", "trade_size"])
        chromosome[mutation_key] = round(random.uniform(1, 10), 1) if mutation_key != "trade_size" else round(random.uniform(10, 30), 1)
    return chromosome

def genetic_algorithm(historical_prices, initial_population, generations=10):
    population = initialize_population(initial_population)
    
    for u in range(generations):
        fitness_scores = [evaluate_fitness(chromosome, historical_prices) for chromosome in population]
        
        new_population = []
        for u in range(len(population) // 2):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
    
    best_strategy = max(population, key=lambda ch: evaluate_fitness(ch, historical_prices))
    final_profit = evaluate_fitness(best_strategy, historical_prices)
    return best_strategy, final_profit


historical_prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
initial_population = [
    {"stop_loss": 2, "take_profit": 5, "trade_size": 20},
    {"stop_loss": 3, "take_profit": 7, "trade_size": 30},
    {"stop_loss": 1.5, "take_profit": 4, "trade_size": 25},
    {"stop_loss": 2.5, "take_profit": 6, "trade_size": 15}
]
generations = 10

best_strategy, final_profit = genetic_algorithm(historical_prices, initial_population, generations)
print("Best Strategy:", best_strategy)
print("Final Profit:", final_profit)
