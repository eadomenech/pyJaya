# -*- coding: utf-8 -*-
from .base import JayaBase
from .clasic import JayaClasic
from pyJaya.population import Population
import numpy as np


class JayaSelfAdadtive(JayaBase):

    def __init__(self, listVars, functionToEvaluate, listConstraints=[]):
        super(JayaSelfAdadtive, self).__init__(
            len(listVars)*10, listVars, functionToEvaluate, listConstraints)

    def nextPopulation(self, population):
        numOldSolutions = population.size()
        numNewSolutions = int(
            round(numOldSolutions*(1 + np.random.rand()-0.5)))

        if numNewSolutions == numOldSolutions:
            return population
        else:
            newPopulation = Population(self.minimax)
            if numNewSolutions < numOldSolutions:
                if numNewSolutions < self.cantVars:
                    numNewSolutions = self.cantVars
                if self.minimax:
                    for solution in population.sorted()[-numNewSolutions:]:
                        newPopulation.solutions.append(solution)
                else:
                    for solution in population.sorted()[:numNewSolutions]:
                        newPopulation.solutions.append(solution)
            elif numNewSolutions > numOldSolutions:
                for solution in population.solutions:
                    newPopulation.solutions.append(solution)
                if self.minimax:
                    begin = numOldSolutions-numNewSolutions
                    for solution in population.sorted()[begin:]:
                        newPopulation.solutions.append(solution)
                else:
                    limit = numNewSolutions-numOldSolutions
                    for solution in population.sorted()[:limit]:
                        newPopulation.solutions.append(solution)
            return newPopulation

    def run(self, numIterations):
        for i in range(numIterations):
            if i > 0:
                self.population = self.nextPopulation(self.population)
            self.population = JayaClasic(
                self.population.size(), self.listVars,
                self.functionToEvaluate, self.listConstraints,
                self.population).run(1)

        return self.population
