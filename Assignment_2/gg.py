import random

# Initialize the population with random chromosomes
def initialize_population(pop_size=4):
    population = []
    for _ in range(pop_size):
        chromosome = {
            "stop_loss": round(random.uniform(1, 10), 1),  # Stop-loss percentage (1 to 10)
            "take_profit": round(random.uniform(1, 10), 1), # Take-profit percentage (1 to 10)
            "trade_size": round(random.uniform(10, 30), 1)  # Trade size percentage (10 to 30)
        }
        population.append(chromosome)
    return population

# Evaluate the fitness of a chromosome based on historical price changes
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

# Select two parents using weighted random selection
def select_parents(population, fitness_scores):
    return random.choices(population, weights=fitness_scores, k=2)

# Perform a one-point crossover
def crossover(parent1, parent2):
    crossover_point = random.choice(["stop_loss", "take_profit", "trade_size"])
    child = parent1.copy()
    child[crossover_point] = parent2[crossover_point]
    return child

# Perform mutation by randomly adjusting one gene
def mutate(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        mutation_key = random.choice(["stop_loss", "take_profit", "trade_size"])
        chromosome[mutation_key] = round(random.uniform(1, 10), 1) if mutation_key != "trade_size" else round(random.uniform(10, 30), 1)
    return chromosome

# Genetic algorithm to evolve the population over several generations
def genetic_algorithm(historical_prices, initial_population, generations=10):
    population = initialize_population(initial_population)
    
    for _ in range(generations):
        fitness_scores = [evaluate_fitness(chromosome, historical_prices) for chromosome in population]
        
        new_population = []
        for _ in range(len(population) // 2):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
    
    best_strategy = max(population, key=lambda ch: evaluate_fitness(ch, historical_prices))
    final_profit = evaluate_fitness(best_strategy, historical_prices)
    return best_strategy, final_profit

# Running the Genetic Algorithm with randomly generated inputs
historical_prices = [round(random.uniform(-5, 5), 2) for _ in range(10)]  # 10 random price changes between -5 and 5
initial_population_size = 4
generations = 10

# Run the genetic algorithm
best_strategy, final_profit = genetic_algorithm(historical_prices, initial_population_size, generations)

# Print the results
print("Historical Prices:", historical_prices)
print("Best Strategy:", best_strategy)
print("Final Profit:", final_profit)
