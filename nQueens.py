import random
import operator
import copy

fitnessNumber = 0
termination = 10000
flag = False


def calculatefitness(population: list, n: int) -> list:
    '''
    :param population: A list of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    '''
    global fitnessNumber
    global flag
    for i in range(0, len(population)):

        if population[i][n] == -1:  # i is one chromosome

            collision = 0
            for j in range(0, n-1):

                for k in range(j+1, n):

                    if abs(population[i][j] - population[i][k]) == abs(j-k):

                        collision = collision + 1

            population[i][n] = 1/(collision + 0.1)
            fitnessNumber += 1  # fitnessNumber is a global variable

    if fitnessNumber >= termination:  # termination is an integer initialized to 10000
        flag = True

    return population


def random_chrom(n: int) -> list:
    '''
    Random chromosome generation
    :param n: number of queens to be placed on the chess board
    :return: randomly generated chromosome.
    '''
    chrom = []  # one chromosome
    for j in range(0, n):
        chrom[j] = random.randint(-1, n-1)  # generating genes randomly for the chromosome
    chrom[n] = -1   # initialising fitness value
    return chrom


def population_gen(population: list, n: int) -> list:
    '''
    Initial population generation
    :param population: initial population of chromosomes
    :param n: number of queens to be placed on the chess board
    :return: fittest two chromosomes out of random five to be sent for crossover.
    '''
    for i in range(0, 100):
        chrom = random_chrom(n)
        population.append(chrom)    # generating 100 random chromosomes as initial population
    new_population = calculatefitness(population, n)    # calculating fitness function
    temp_population = []
    for i in range(0, 5):
        temp_population.append(new_population[random.randint(-1, 99)])  # five randomly chosen chromosomes
    sorted(temp_population, key=operator.itemgetter(n))     # fittest two chromosomes picked out of five
    crossover_pop = []
    for i in range(0, 2):
        crossover_pop.append(temp_population[i])
    return crossover_pop


def mutation(permutation):
    n = len(permutation[0])
    rnd = random.random()
    mutation_prob = 0.8
    if rnd < mutation_prob:
        loci1 = random.randint(0, n - 2)
        loci2 = random.randint(0, n - 2)
        while loci2 == loci1:
            loci2 = random.randint(0, n - 2)
        result = copy.deepcopy(permutation)
        result[0][loci1], result[0][loci2] = result[0][loci2], result[0][loci1]
        result[1][loci1], result[1][loci2] = result[1][loci2], result[1][loci1]
        return result
    return permutation

