import numpy as np
import math
import random


class pbil(object):
    def __init__(self, imgMAT, oimgMAt, LR=0.2, MS=0.05, shouldMutate=True, rowSize=5, colSize=5, FL=1):
        self.PV = np.full((1, colSize), 0.5)
        self.n = rowSize
        self.m = colSize
        self.imgMAT = imgMAT
        self.pop = np.random.choice(2, rowSize * colSize, self.PV.tolist()).reshape(rowSize, colSize)
        self.TimgMAT = np.random.uniform(low=0, high=0, size=(rowSize, colSize))
        self.fitness = np.zeros(colSize)
        self.best_chromosome_index = -1
        self.best_chromosome_list = np.array
        self.LR = LR
        self.MS = MS
        self.oimgMAT = oimgMAt
        self.FL = FL
        self.shouldMutate = shouldMutate

    def printData(self):
        print('Probability_vector=\n', self.PV)
        print('Population=\n', self.pop)
        print('Image =\n', self.imgMAT)
        print('Translated/Truncated Image =\n', self.TimgMAT)

    def translateImg(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.pop[i][j] == 1:
                    self.TimgMAT[i][j] = math.trunc(self.imgMAT[i][j]) + 1
                else:
                    self.TimgMAT[i][j] = math.trunc(self.imgMAT[i][j])

    def calculate_fitness(self):
        self.fitness = np.zeros(self.m)
        for i in range(self.n):
            for j in range(self.m):
                self.fitness[i] += int(abs(self.TimgMAT[i][j] - round(self.imgMAT[i][j])))
        self.best_chromosome_index = np.where(self.fitness == np.amin(self.fitness))
        self.best_chromosome_list = [i for i in self.pop[self.best_chromosome_index[0]].tolist()]

    def update_PV(self):
        Solution_Vector = self.best_chromosome_list[0]
        for i in range(len(self.PV)):
            self.PV[i] = self.PV[i] * (1 - self.LR) + Solution_Vector[i] * self.LR

    def mutate_PV(self):
        for i in range(len(self.PV)):
            self.PV[i] = self.PV[i] * (1 - self.MS) + random.randint(0, 1) * self.LR

    def Generate(self):
        while True:
            self.pop = np.random.choice(2, self.n * self.m, self.PV.tolist()).reshape(self.n, self.m)
            self.translateImg()
            self.calculate_fitness()
            self.update_PV()
            if self.shouldMutate:
                self.mutate_PV()
            BC = self.best_chromosome_list
            if len(BC) == self.n and np.amin(self.fitness) <= self.FL:
                break
        self.printData()
