import random
import operator
import copy

fitnessNumber = 0
termination = 25


def random_chrom(n: int) -> list:
    """
    Random chromosome generation
    :param n: The number of queens to be placed on the chess board
    :return: randomly generated chromosome.
    """
    chrom = []  # one chromosome
    j = 0
    while True:
        temp = random.randint(0, n-1)
        if temp not in chrom:
            chrom.append(temp)   # generating genes randomly for the chromosome
            j += 1
        if j == n:
            break
    chrom.append(-1)   # initialising fitness value
    return chrom


def calculatefitness(population: list, n: int, args: dict) -> list:
    """
    :param population: A list of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    """
    for i in range(0, len(population)):
        if population[i][n-1] == -1:
            population[i][n-1] = 0
            for j in range(0, n-1):
                if population[i][j] == 1:
                    population[i][n-1] += args[j][0]
    return population


def population_gen(population: list, count: int, n: int) -> list:
    """
    Initial population generation
    :param population: initial population of chromosomes
    :param count: count of the generation created
    :param n: The number of queens to be placed on the chessboard
    :return: fittest two chromosomes out of random five to be sent for crossover.
    """
    if count == 1:
        for i in range(0, 100):
            chrom = random_chrom(n)
            population.append(chrom)    # generating 100 random chromosomes as initial population
        new_population = calculatefitness(population, n)    # calculating fitness function
    else:
        new_population = population
    temp_population = []
    for i in range(0, 5):
        temp_population.append(new_population[random.randint(0, 99)])  # five randomly chosen chromosomes
    temp_population.sort(key=operator.itemgetter(n), reverse=True)     # fittest two chromosomes picked out of five
    crossover_pop = []
    for i in range(0, 2):
        crossover_pop.append(temp_population[i])
    return crossover_pop


def crossover(parents: list, recomb_prob: float, n: int) -> list:
    """
    :param parents: list of chromosomes involved in crossover
    :param recomb_prob: Recombination probability
    :param n: The number of queens to be placed on the chessboard
    :return: children created by crossover
    """
    pass


def mutation(permutation: list, mutation_prob: float, n: int) -> list:
    """"
    :param permutation: chromosome post recombination
    :param mutation_prob: mutation probability
    :param n: The number of queens to be placed on the chessboard
    :return: mutated chromosome
    """
    pass


def selection(population: list, n: int) -> list:
    """
    :param population: chromosome population post crossover and mutation
    :param n: The number of queens to be placed on the chessboard
    :return: best hundred of the population
    """
    population.sort(key=operator.itemgetter(n), reverse=True)
    population = population[:len(population) - 2]
    return population


def main():
    n = int(input("Enter the value of n"))
    recomb_prob = float(input("Enter the value of recombination probability"))
    mutation_prob = float(input("Enter the value of mutation probability"))

    population = []
    count = 1
    while True:
        crossover_val = population_gen(population, count, n)
        crossover_pop = crossover(crossover_val, recomb_prob, n)
        children = mutation(crossover_pop, mutation_prob, n)
        i = 0
        while i != 2:
            population.append(children[i])
        population = selection(population, n)
        count += 1


main()

