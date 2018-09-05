import random
import operator

gen_no = 0
termination = 25
past_gen = []   # stores the previous generation


def random_chrom(args: dict, total_weight: float, n: int) -> list:
    """
    Random chromosome generation
    :param args: Info regarding weight and value of each item
    :param total_weight: Total weight capacity of knapsack
    :param n: The total number of items available
    :return: randomly generated chromosome.
    """
    chrom = []  # one chromosome
    j = 0
    while True:
        temp = random.randint(0, 1)
        chrom.append(temp)   # generating genes randomly for the chromosome
        j += 1
        if j == n:
            if cal_weight(chrom, args, n) <= total_weight:
                break
            else:
                j = 0
    chrom.append(-1)   # initialising fitness value
    return chrom


def calculatefitness(population: list, args: dict, n: int) -> list:
    """
    Calculating fitness value
    :param population: A list of chromosomes
    :param args: Info regarding weight and value of each item
    :param n: The total number of items available
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    """
    for i in range(0, len(population)):
        if population[i][n] == -1:    # calculate fitness (total value) of set of chosen items if not already calculated
            population[i][n] = 0
            for j in range(0, n):
                population[i][n] += (population[i] * args[j][1])
    return population


def cal_weight(chrom: list, args: dict, n: int) -> float:
    """
    Calculating total weight of chosen items
    :param chrom: one chromosome
    :param args: Info regarding weight and value of each item
    :param n: The total number of items available
    :return: total weight of chromosome
    """
    wt = 0
    for i in range(0, n):
        wt += (chrom[i] * args[i][0])
    return wt


def population_gen(population: list, args: dict, total_weight: float, n: int):
    """
    Initial population generation
    :param population: initial population of chromosomes
    :param args: Info regarding weight and value of each item
    :param total_weight: Total weight capacity of knapsack
    :param n: The total number of items available
    :return: Fittest two chromosomes out of random five to be sent for crossover.
    """
    for i in range(0, 100):
        chrom = random_chrom(args, total_weight, n)
        population.append(chrom)  # generating 100 random chromosomes as initial population
        population = calculatefitness(population, args, n)  # calculating fitness function


def crossover_sel(population: list, n: int) -> list:
    """
    Selecting parents for crossover
    :param population: population of chromosomes
    :param n: The total number of items available
    :return: Chromosomes selected for crossover
    """
    temp_population = []
    temp_index = []
    i = 0
    while i < 5:
        j = random.randint(0, 99)
        if j not in temp_index:
            temp_index.append(j)
            temp_population.append(population[j])  # five randomly chosen chromosomes
            i += 1
    temp_population.sort(key=operator.itemgetter(n), reverse=True)  # fittest two chromosomes picked out of five
    crossover_pop = []
    for i in range(0, 2):
        crossover_pop.append(temp_population[i])
    return crossover_pop


def crossover(parents: list, recomb_prob: float, args: dict, n: int) -> list:
    """
    One point crossover
    :param parents: list of chromosomes involved in crossover
    :param recomb_prob: Recombination probability
    :param args: Info regarding weight and value of each item
    :param n: The total number of items available
    :return: children created by crossover
    """
    rnd = random.random()  # picking a random number between 0 and 1
    index = random.randint(0, n - 1)
    children = []
    if rnd <= recomb_prob:
        for i in range(0, 2):
            temp_children = []
            if index == 0:
                temp_children = parents[(i+1) % 2]    # Children remain the same as parents in the opposite index
            elif index == n:
                temp_children = parents[i]  # Children remain the same as parents
            else:
                for j in range(0, index):
                    temp_children.append(parents[i][j])   # Copying genes from parent to child until position 'index'
                for j in range(index, n):
                    temp_children.append(parents[(i+1) % 2][j])     # Copying remaining genes from other parent to child
            if len(temp_children) != n + 1:
                temp_children.append(-1)
            children.append(temp_children)

        children = calculatefitness(children, args, n)
        return children
    return parents


def mutation(population: list, mutation_prob: float, n: int) -> list:
    """"
    Bit flipping mutation in created children
    :param population: Chromosome post recombination
    :param mutation_prob: Mutation probability
    :param n: The total number of items available
    :return: Mutated chromosome
    """
    if random.randint(0, 10) < mutation_prob * 10:
        for i in range(0, len(population)):
            x = random.randint(0, n-1)
            if population[i][x] == 0:
                population[i][x] = 1
            else:
                population[i][x] = 0

    return population


def selection(population: list, n: int) -> list:
    """
    Selecting fittest 100 chromosomes
    :param population: Chromosome population post crossover and mutation
    :param n: The total number of items available
    :return: Best hundred of the population
    """
    global gen_no
    global past_gen
    population.sort(key=operator.itemgetter(n), reverse=True)
    population = population[:len(population) - 2]   # removing least fittest two from population
    if population == past_gen:  # checking if previous generation was same as current generation
        gen_no += 1
        if gen_no == 25:    # termination condition
            print("The final answer is")
            print("Chromosome:")
            chrom = []
            for i in range(0, n):
                chrom.append(population[0][i])
            print(chrom)
            print("Fitness value:")
            print(population[0][n])
            exit()
    else:
        gen_no = 0
        past_gen = population
    return population


def main():
    population = []
    count = 1
    print("Enter the number of items")
    n = int(input())
    print("Enter the value of recombination probability")
    recomb_prob = float(input())
    print("Enter the value of mutation probability")
    mutation_prob = float(input())
    print("Enter the total weight capacity")
    total_weight = float(input())
    args = {}
    for i in range(0, n):
        print("Enter the weight of item", i+1)
        item_wt = float(input())
        print("Enter the value of item", i + 1)
        item_val = float(input())
        args[i].append((item_wt, item_val))     # args = { index : (item_wt,item_val) }
    population_gen(population, args, total_weight, n)
    while True:
        crossover_val = crossover_sel(population, n)
        crossover_pop = crossover(crossover_val, recomb_prob, args, n)
        children = mutation(crossover_pop, mutation_prob, n)
        i = 0
        while i != 2:
            population.append(children[i])
        population = selection(population, n)
        count += 1


main()

