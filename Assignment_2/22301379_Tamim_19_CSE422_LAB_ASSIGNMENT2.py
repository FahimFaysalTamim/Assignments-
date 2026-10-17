import random


def initialize_population(size=4):
    population = []
    for i in range(size):
        chromosome = {
            "stop_loss": round(random.uniform(1, 10), 1),  
            "take_profit": round(random.uniform(1, 10), 1), 
            "trade_size": round(random.uniform(10, 30), 1)  
        }
        population.append(chromosome)
    return population


def evaluate_fitness(chromosome, historical_prices, initial_capital=1000):
    capital = initial_capital
    for price_change in historical_prices:
        trade_amount = capital * (chromosome["trade_size"] / 100)
        
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
    
    for i in range(generations):
        fitness_scores = [evaluate_fitness(chromosome, historical_prices) for chromosome in population]
        
        new_population = []
        for j in range(len(population) // 2):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
    
    best_strategy = max(population, key=lambda ch: evaluate_fitness(ch, historical_prices))
    final_profit = evaluate_fitness(best_strategy, historical_prices)
    return best_strategy, final_profit


historical_prices = [round(random.uniform(-5, 5), 2) for i in range(10)]  
initial_population_size = 4
generations = 10


best_strategy, final_profit = genetic_algorithm(historical_prices, initial_population_size, generations)

#
print("Historical Prices:", historical_prices)
print("Best Strategy:", best_strategy)
print("Final Profit:", final_profit)
