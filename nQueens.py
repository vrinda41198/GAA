import random
import operator
import copy

fitnessNumber = 0
termination = 10000
flag = False


def random_chrom(n: int) -> list:
    """
    Random chromosome generation
    :param n: number of queens to be placed on the chess board
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
    print(chrom)
    return chrom


def calculatefitness(population: list, n: int) -> list:
    """
    :param population: A list of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    """
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


def population_gen(population: list, count: int, n: int) -> list:
    """
    Initial population generation
    :param population: initial population of chromosomes
    :param count: count of the generation created
    :param n: number of queens to be placed on the chess board
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
    print(temp_population)
    print("HAHA")
    crossover_pop = []
    for i in range(0, 2):
        crossover_pop.append(temp_population[i])
    return crossover_pop


def crossover(parents: list, n: int) -> list:
    """
    :param parents: list of chromosomes involved in crossover
    :param n: length of one chromosome
    :return: children created by crossover
    """
    cross_point = random.randint(0, n)
    index = cross_point
    children = []
    for i in range(0, 2):
        print(index)
        if index == 0:
            children[i] = parents[(i+1) % 2]
        elif index == n:
            children[i] = parents[i]
        else:
            for j in range(0, index):
                children[i].append(parents[i][j])
            k = index
            j = index
            while j < n:
                val = parents[((i + 1) % 2)][k]
                if val not in children[0:index]:
                    children[i].append(val)
                    j += 1
                k = (k+1) % n

    return children


def mutation(permutation: list, mutation_prob: float) -> list:
    """"
    :param permutation: chromosome post recombination
    :param mutation_prob: mutation probability
    :return: mutated chromosome
    """
    n = len(permutation[0])
    rnd = random.random()
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


def selection(population: list, n: int) -> list:
    """
    :param population: chromosome population post crossover and mutation
    :param n: length of the chromosome
    :return: best hundred of the population
    """
    population.sort(key=operator.itemgetter(n), reverse=True)
    population = population[:len(population) - 2]
    return population


def main():
    n = int(input("Enter the value of n"))
    mutation_prob = float(input("Enter the value of mutation probability"))
    population = []
    count = 1
    while True:
        crossover_val = population_gen(population, count, n)
        crossover_pop = crossover(crossover_val, n)
        children = mutation(crossover_pop, mutation_prob)
        i = 0
        while i != 2:
            population.append(children[i])
        population = selection(population, n)
        count += 1

        
main()
