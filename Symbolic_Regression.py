import random

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

def parent_selection(population: list, x: int, y: int) -> list
    """
    To select parents for crossover using overselection
    :param population:
    :param x:
    :param y:
    """
    group1 = []
    group2 = []
    return population


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