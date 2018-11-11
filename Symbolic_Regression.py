import random
import operator
import math

u = 0.32
v = 0.80

def randomxy(x: list, y: list):
    """
    To generate 100 random values of x and y
    :param x:
    :param y:
    :return:
    """
    pass


def parse_gen(chrom: list, func_set: dict, term_set: dict):
    """
    To generate one parse tree
    :param chrom:
    :param func_set:
    :param term_set:
    :return:
    """
    pass


def pop_gen(func_set: dict, term_set: dict):
    """
    To generate  thousand random parse trees
    :param func_set:
    :param term_set:
    :return:
    """
    pass


def fitness_evaluation(chrom: list, x: list, y: list) -> float:
    """
    To evaluate fitness value of each parse tree
    :param chrom:
    :param x:
    :param y:
    :return:
    """
    pass

def parent_selection(population: list, n: int) -> list:
    """
    To select parents for crossover using overselection
    :param population:
    :param x:
    :param y:
    """
    temp_population = []

    index1 = math.floor(u*len(population))

    population.sort(key=operator.itemgetter(n), reverse=True)
    group1 = population[:index1]
    group2 = population[index1+1:]

    index2 = math.floor(v*len(group1))
    index3 = math.floor((1-v)*len(group2))

    temp_population.append(group1[:index2])
    temp_population.append(group2[:index3])
    temp_population.sort(key=operator.itemgetter(n), reverse=True)

    parents = temp_population[:2]

    return parents

def subtree_recomb(parents: list, recomb_prob: float) -> list:
    """
    To generate children after applying sub-tree crossover on parents
    :param parents:
    :param recomb_prob:
    :param n:
    """
    index = []
    temp = []

    for i in range(0, 2):
        index[i] = random.randint(0, len(parents[i]))
        temp[i] = parents[index[i]:]

    for j in range(0, 2):
        del parents[j][index[j]:]
        parents[j].append(temp[(j+1)%2])

    return parents


def selection() :
    pass