import numpy as np


def min_dis(target,source):
    target=[k for k in target]
    source=[k for k in source]
    solution=np.zeros((len(source),len(target)))

    #row and column
    solution[0]=[ j for j in range(len(target))]
    solution[:,0]=[j for j in range(len(source))]

    if target[1] != source[1]:
        solution[1,1]=2

    k=1
    for c in range(1, len(target)):

        for r in range(1,len(source)):

            if target[c] != source[r]:
                solution[r,c]=min(solution[r-1,c],solution[r,c-1])+1

            else:
                solution[r,c]=solution[r-1,c-1]
            print(f"{k}:{solution}\n")
            k+=1
    return solution

print(min_dis("#setting","#meeting"))

input("press a button")

