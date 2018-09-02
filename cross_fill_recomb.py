import random


def crossover(parents, n):
    cross_point = random.randint(0,n)
    index = cross_point
    children = [[], []]

    for i in range(0,2):
        print(index)
        if index == 0:
            children[i] = parents[(i+1)%2]
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
                k = (k+1)%n

    return children


def main():
    check_list = crossover([[1,3,5,2,6,4,7,8], [8,7,6,5,4,3,2,1]], 8)
    print(check_list[0])
    print(2)
    print(check_list[1])












