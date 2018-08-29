def CalculateFitness(population:list,n:int) -> list:

    for i in range(0,len(population)):

        if i[n]==-1:  #i is one chromosome

            collision = 0
            for j in range(0,n-1):

                for k in range(j+1,n):

                    if abs(i[j]-i[k])==abs(j-k):

                        collision = collision + 1

            i[n]=1/(collision+0.1)
            fitnessNumber = fitnessNumber + 1   #fitnessNumber is a global variable

    if fitnessNumber >= termination:  #termination is an integer initialized to 10000
        flag = True

    return population











