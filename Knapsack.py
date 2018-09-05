import random
import operator
import copy

gen_no = 0
termination = 25
past_gen = []   # stores the previous generation


def calculatefitness(population: list, args: dict, n: int) -> list:
    """
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
    :param chrom: one chromosome
    :param args: Info regarding weight and value of each item
    :param n: The total number of items available
    :return: total weight of chromosome
    """
    wt = 0
    for i in range(0, n):
        wt += (chrom[i] * args[i][0])
    return wt


def population_gen(population: list, args: dict, total_weight: float, n: int) -> list:
    """
    Initial population generation
    :param population: initial population of chromosomes
    :param args: Info regarding weight and value of each item
    :param total_weight: Total weight capacity of knapsack
    :param n: The total number of items available
    :return: Fittest two chromosomes out of random five to be sent for crossover.
    """
    pass


def crossover_sel(population: list, n: int) -> list:
    """
    :param population: population of chromosomes
    :param n: The total number of items available
    :return: Chromosomes selected for crossover
    """
    pass


def crossover(parents: list, recomb_prob: float, args: dict, n: int) -> list:
    """
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
    :param population: Chromosome post recombination
    :param mutation_prob: Mutation probability
    :param n: The total number of items available
    :return: Mutated chromosome
    """
    if random.randint(0, 10) < mutation_prob*10:
        for i in range(0, len(population)):
            x = random.randint(0, n-1)
            if population[i][x]==0:
                population[i][x]=1
            else:
                population[i][x]=0

    return population


def selection(population: list, n: int) -> list:
    """
    :param population: Chromosome population post crossover and mutation
    :param n: The total number of items available
    :return: Best hundred of the population
    """
    global gen_no
    global past_gen
    population.sort(key=operator.itemgetter(n), reverse=True)
    population = population[:len(population) - 2]   # removing least fittest two from population
    if population == past_gen:
        gen_no += 1
        if gen_no == 25:
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
    n = int(input("Enter the number of items"))
    recomb_prob = float(input("Enter the value of recombination probability"))
    mutation_prob = float(input("Enter the value of mutation probability"))
    total_weight = float(input("Enter the total weight capacity"))
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

