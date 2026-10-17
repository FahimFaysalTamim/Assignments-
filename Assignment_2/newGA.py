import random

# Parameters
INITIAL_CAPITAL = 1000
HISTORICAL_PRICES = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
INITIAL_POPULATION = [
    {"stop_loss": 2, "take_profit": 5, "trade_size": 20},
    {"stop_loss": 3, "take_profit": 7, "trade_size": 30},
    {"stop_loss": 1.5, "take_profit": 4, "trade_size": 25},
    {"stop_loss": 2.5, "take_profit": 6, "trade_size": 15}
]
GENERATIONS = 10
MUTATION_RATE = 0.05

# Fitness function
def calculate_fitness(chromosome):
    capital = INITIAL_CAPITAL
    for price in HISTORICAL_PRICES:
        trade_size = capital * (chromosome["trade_size"] / 100)
        if price <= -chromosome["stop_loss"]:
            capital -= trade_size * (chromosome["stop_loss"] / 100)
        elif price >= chromosome["take_profit"]:
            capital += trade_size * (chromosome["take_profit"] / 100)
        else:
            capital += trade_size * (price / 100)
    return capital - INITIAL_CAPITAL

# Selection
def select_parents(population):
    return random.sample(population, 2)

# Crossover
def crossover(parent1, parent2):
    split_point = random.randint(1, 2)
    print(split_point)
    child1 = {
        "stop_loss": parent1["stop_loss"] if split_point == 1 else parent2["stop_loss"],
        "take_profit": parent1["take_profit"] if split_point == 1 else parent2["take_profit"],
        "trade_size": parent1["trade_size"] if split_point == 2 else parent2["trade_size"]
    }
    child2 = {
        "stop_loss": parent2["stop_loss"] if split_point == 1 else parent1["stop_loss"],
        "take_profit": parent2["take_profit"] if split_point == 1 else parent1["take_profit"],
        "trade_size": parent2["trade_size"] if split_point == 2 else parent1["trade_size"]
    }
    return child1, child2

# Mutation
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        chromosome["stop_loss"] = random.uniform(1, 99)
    if random.random() < MUTATION_RATE:
        chromosome["take_profit"] = random.uniform(1, 99)
    if random.random() < MUTATION_RATE:
        chromosome["trade_size"] = random.uniform(1, 99)
    return chromosome

# Genetic Algorithm
def genetic_algorithm():
    population = INITIAL_POPULATION.copy()
    for generation in range(GENERATIONS):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
        best_index = fitness_scores.index(max(fitness_scores))
        best_chromosome = population[best_index]
        
        # Create new population
        new_population = [best_chromosome]  # Elitism
        while len(new_population) < len(population):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
    
    # Return best strategy
    best_fitness = max([calculate_fitness(chromosome) for chromosome in population])
    best_chromosome = population[[calculate_fitness(chromosome) for chromosome in population].index(best_fitness)]
    return {
        "best_strategy": best_chromosome,
        "final_profit": best_fitness
    }

# Run the algorithm
result = genetic_algorithm()
print(result)