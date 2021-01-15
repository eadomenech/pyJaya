# -*- coding: utf-8 -*-
import numpy as np

from pyJaya.variants.base import JayaBase
from pyJaya.variants.clasic import JayaClasic
from pyJaya.population import Population


class JayaSelfAdaptive(JayaBase):
    """Jaya Self-adaptive class

    Args:
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        listConstraints (list, optional): Constraint list. Defaults to [].
    """

    def __init__(
            self, listVars, functionToEvaluate, listConstraints=[],
            population=None):
        super(JayaSelfAdaptive, self).__init__(
            len(listVars)*10, listVars, functionToEvaluate, listConstraints,
            population=population)

    def nextPopulation(self, population):
        """New population.

        Returns:
            Population: Next population.
        """
        numOldSolutions = population.size()
        r = 1 + (np.random.rand()-0.5)
        numNewSolutions = round(numOldSolutions * r)

        if numNewSolutions == numOldSolutions:
            return population
        else:
            newPopulation = Population(self.minimax, solutions=[])
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

    def run(self, number_iterations, rn=[]):
        """Run method

        Args:
            number_iterations (int): Number of iterations.

        Returns:
            Population: Final population.
        """
        if len(rn) == 0:
            self.rn = self.generate_rn(number_iterations)
        else:
            assert number_iterations == len(rn)
            assert len(rn[0]) == self.cantVars
            assert len(rn[0][0]) == 2
            self.rn = rn
        for i in range(number_iterations):
            if i > 0:
                self.population = self.nextPopulation(self.population)
            self.population = JayaClasic(
                self.population.size(), self.listVars,
                self.functionToEvaluate, listConstraints=self.listConstraints,
                population=self.population).run(1, [self.rn[i]])

        return self.population
