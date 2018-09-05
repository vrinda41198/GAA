import random
import operator
import copy

fitnessNumber = 0
termination = 25


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
                if population[i][j] == 1:       # add the value of an item to the fitness func if it's chosen
                    population[i][n] += args[j][1]
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


def crossover(parents: list, recomb_prob: float, n: int) -> list:
    """
    :param parents: list of chromosomes involved in crossover
    :param recomb_prob: Recombination probability
    :param n: The total number of items available
    :return: children created by crossover
    """
    pass


def mutation(population: list, mutation_prob: float, n: int) -> list:
    """"
    :param population: Chromosome post recombination
    :param mutation_prob: Mutation probability
    :param n: The total number of items available
    :return: Mutated chromosome
    """
    pass


def selection(population: list, n: int) -> list:
    """
    :param population: Chromosome population post crossover and mutation
    :param n: The total number of items available
    :return: Best hundred of the population
    """
    pass


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
        crossover_pop = crossover(crossover_val, recomb_prob, n)
        children = mutation(crossover_pop, mutation_prob, n)
        i = 0
        while i != 2:
            population.append(children[i])
        population = selection(population, n)
        count += 1


main()

