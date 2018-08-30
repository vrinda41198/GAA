def mutation(permutation):
    n = len(permutation)
    rnd = random.random()
    mutation_prob = 0.8
    if rnd < mutation_prob:
        loci1 = random.randint(0, n - 1)
        loci2 = random.randint(0, n - 1)
        while loci2 == loci1:
            loci2 = random.randint(0, n - 1)
        result = copy.deepcopy(permutation)
        result[loci1], result[loci2] = result[loci2], result[loci1]
        return result
    return permutation