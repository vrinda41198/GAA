import random
import copy

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