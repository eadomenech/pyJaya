# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
import numpy as np


class JayaSelfAdadtive(JayaBase):

    def __init__(self, listVars, functionToEvaluate, listConstraints=[]):
        super(JayaSelfAdadtive, self).__init__(
            len(listVars)*10, listVars, functionToEvaluate, listConstraints)

    def nextPopulation(self, population):
        numOldSolutions = len(population.solutions)
        numNewSolutions = int(round(numOldSolutions*(1 + np.random.rand()-0.5)))

        if numNewSolutions == numOldSolutions:
            return population
        else:
            newPopulation = Population(self.minimax)
            if numNewSolutions < numOldSolutions:
                if numNewSolutions < self.cantVars:
                    numNewSolutions = self.cantVars
                if self.minimax:
                    for solution in population.sorted()[-numNewSolutions:]:
                        newPopulation.solution.append(solution)
                else:
                    for solution in population.sorted()[:numNewSolutions]:
                        newPopulation.solutions.append(solution)
            elif numNewSolutions > numOldSolutions:
                for solution in population.solutions:
                    newPopulation.solutions.append(solution)
                if self.minimax:
                    for solution in population.sorted()[numOldSolutions-numNewSolutions:]:
                        newPopulation.solution.append(solution)
                else:
                    for solution in population.sorted()[:numNewSolutions-numOldSolutions]:
                        newPopulation.solutions.append(solution)
            return newPopulation

    def run(self, numIterations):
        for i in range(numIterations):
            if i > 0:
                self.population = self.nextPopulation(self.population)
            result = self.population.getBestAndWorst()
            for solution in self.population.solutions:
                solt = []
                for v_item, v_value in enumerate(solution.solution):
                    r1 = np.random.rand(self.cantVars)
                    r2 = np.random.rand(self.cantVars)
                    solt.append(self.listVars[v_item].convert(
                        (v_value+r1[v_item] * (result['best_solution'][v_item] - abs(v_value)) - r2[v_item] * (result['worst_solution'][v_item]-abs(v_value)))
                    ))
                auxSolution = Solution(
                    self.listVars, self.functionToEvaluate,
                    self.listConstraints)
                auxSolution.setSolution(np.array(solt))
                if self.minimax:
                    if (auxSolution.value > solution.value) and \
                            (auxSolution.constraintsOK(np.array(solt))):
                        solution = auxSolution
                else:
                    if (auxSolution.value < solution.value) and \
                            (auxSolution.constraintsOK(np.array(solt))):
                        solution.setSolution(auxSolution.solution)

        return self.population.getBestAndWorst()
