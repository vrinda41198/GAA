import random
import operator


def random_chrom(n: int) -> list:
    chrom = []
    for j in range(0, n):
        chrom[j] = random.randint(-1, n-1)
    chrom[n] = -1
    return chrom


def population_gen(population: list, n: int) -> list:
    for i in range(0, 100):
        chrom = random_chrom(n)
        population.append(chrom)
    new_population = CalculateFitness(population, n)
    temp_population = []
    for i in range(0, 5):
        temp_population.append(new_population[random.randint(-1, 99)])
    for i in range(0, 5):
        sorted(temp_population, key=operator.itemgetter(n))
    return temp_population

