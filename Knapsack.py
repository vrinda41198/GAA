import random
import operator
import copy

fitnessNumber = 0
termination = 25


def calculatefitness(population: list, n: int) -> list:
    """
    :param population: A list of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    """
    pass


def cal_weight(chrom: list, args: dict, n: int) -> float:
    """
    :param chrom: one chromosome
    :param args: info regarding weight and value of each item
    :return: total weight of chromosome
    """
    wt = 0
    for i in range(0, n):
        wt += (chrom[i] * args[i][0])
    return wt


def population_gen(population: list, count: int, n: int) -> list:
    """
    Initial population generation
    :param population: initial population of chromosomes
    :param count: count of the generation created
    :param n: The number of queens to be placed on the chessboard
    :return: fittest two chromosomes out of random five to be sent for crossover.
    """
    pass


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

    while True:
        crossover_val = population_gen(population, args, total_weight, n)
        crossover_pop = crossover(crossover_val, recomb_prob, n)
        children = mutation(crossover_pop, mutation_prob, n)
        i = 0
        while i != 2:
            population.append(children[i])
        population = selection(population, n)
        count += 1


main()

