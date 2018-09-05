import random
import operator
import copy

fitnessNumber = 0
termination = 10000


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


def calculatefitness(population: list, n: int) -> list:
    """
    Calculating fitness value
    :param population: A list of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: The list of chromosomes with their fitness stored at the end of each chromosome
    """
    global fitnessNumber
    for i in range(0, len(population)):

        if population[i][n] == -1:  # i is one chromosome

            collision = 0
            for j in range(0, n-1):

                for k in range(j+1, n):

                    if abs(population[i][j] - population[i][k]) == abs(j-k):

                        collision = collision + 1

            population[i][n] = round((1/(collision + 0.1)),2)
            fitnessNumber += 1  # number of fitness functions calculated

    if fitnessNumber >= termination:  # termination condition
        population.sort(key=operator.itemgetter(n), reverse=True)
        print("The final answer is")
        print("Chromosome:")
        chrom = []
        for i in range(0, n):
            chrom.append(population[0][i])
        print(chrom)
        print("Fitness value:")
        print(population[0][n])
        exit()

    return population


def population_gen(population: list, n: int):
    """
    Initial population generation
    :param population: Initial population of chromosomes
    :param n: The number of queens to be placed on the chessboard
    :return: Fittest two chromosomes out of random five to be sent for crossover.
    """
    for i in range(0, 100):
        chrom = random_chrom(n)
        population.append(chrom)    # generating 100 random chromosomes as initial population
        population = calculatefitness(population, n)    # calculating fitness function


def crossover_sel(population: list, n: int) -> list:
    """
    Selecting parents for crossover
    :param population: Population of chromosomes
    :param n: The number of queens to be placed on the chessboard
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
    temp_population.sort(key=operator.itemgetter(n), reverse=True)     # fittest two chromosomes picked out of five
    crossover_pop = []
    for i in range(0, 2):
        crossover_pop.append(temp_population[i])
    return crossover_pop


def crossover(parents: list, recomb_prob: float, n: int) -> list:
    """
    Crossover between parents
    :param parents: List of chromosomes involved in crossover
    :param recomb_prob: Recombination probability
    :param n: The number of queens to be placed on the chessboard
    :return: Children created by crossover
    """
    rnd = random.random()  # picking a random number between 0 and 1
    index = random.randint(0, n-1)
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
                k = index
                j = index
                while j < n:                           # to fill the remaining genes of the child
                    val = parents[((i + 1) % 2)][k]    # genes of parents post the position 'index'
                    if val not in temp_children[0:j]:
                        temp_children.append(val)
                        j += 1
                    k = (k+1) % n
            if len(temp_children) != n+1:
                temp_children.append(-1)
            children.append(temp_children)

        return children
    return parents


def mutation(population: list, mutation_prob: float, n: int) -> list:
    """"
    Mutation in created children
    :param population: Chromosome post recombination
    :param mutation_prob: Mutation probability
    :param n: The number of queens to be placed on the chessboard
    :return: Mutated chromosome
    """
    rnd = random.random()   # picking a random number between 0 and 1
    if rnd < mutation_prob:     # checking if mutation is allowed
        loci1 = random.randint(0, n - 1)
        loci2 = random.randint(0, n - 1)    # picking two mutation points in each chromosome
        while loci2 == loci1:
            loci2 = random.randint(0, n - 1)
        result = copy.deepcopy(population)
        result[0][loci1], result[0][loci2] = result[0][loci2], result[0][loci1]
        result[1][loci1], result[1][loci2] = result[1][loci2], result[1][loci1]     # performing swap mutation
        return result
    return population  # returning unmutated population in case mutation does not occur


def selection(population: list, n: int) -> list:
    """
    Selecting top 100 chromosomes
    :param population: Chromosome population post crossover and mutation
    :param n: The number of queens to be placed on the chessboard
    :return: Best hundred of the population
    """
    population.sort(key=operator.itemgetter(n), reverse=True)
    population = population[:len(population) - 2]   # removing least fittest two from population
    return population


def main():
    print("Enter the value of n")
    n = int(input())
    print("Enter the value of recombination probability")
    recomb_prob = float(input())
    print("Enter the value of mutation probability")
    mutation_prob = float(input())

    population = []
    population_gen(population, n)
    while True:
        crossover_val = crossover_sel(population, n)
        print("Crossover parents")
        print(crossover_val)
        crossover_pop = crossover(crossover_val, recomb_prob, n)
        print("Crossover complete.")
        print("Crossover children")
        print(crossover_pop)
        children = mutation(crossover_pop, mutation_prob, n)
        print("Mutation complete.")
        i = 0
        while i != 2:
            population.append(children[i])
            i += 1
        population = calculatefitness(population, n)
        print("Mutated children")
        print(population[100], population[101])
        population = selection(population, n)

        
main()


