# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
import numpy as np


class JayaQuasiOppositional(JayaBase):

    def generateQuasiOpposite(self, population):
        newPopulation = Population(self.minimax)
        for solution in population.solutions:
            newSolution = Solution(
                self.listVars, self.functionToEvaluate, self.listConstraints)
            newsolution = []
            for solt_item, solt_value in enumerate(solution.solution):
                AL = self.listVars[solt_item].minor
                AU = self.listVars[solt_item].major
                a = self.listVars[solt_item].convert((AL + AU) / 2)
                b = self.listVars[solt_item].convert(AL + AU - solt_value)
                val = (max(a, b) - min(a, b)) * np.random.random_sample() + min(a, b)
                newsolution.append(self.listVars[solt_item].convert(val))
            newSolution.setSolution(newsolution)
            newPopulation.solutions.append(newSolution)
        return newPopulation

    def newPopulation(self):
        auxPopulation = Population(self.minimax)
        quasiOppositePopulation = self.generateQuasiOpposite(self.population)
        for s in self.population.solutions:
            auxPopulation.solutions.append(s)
        for s in quasiOppositePopulation.solutions:
            auxPopulation.solutions.append(s)
        newPopulation = Population(self.minimax)
        if self.minimax:
            for s in auxPopulation.sorted()[-self.numSolutions:]:
                newPopulation.solutions.append(s)
        else:
            for s in auxPopulation.sorted()[:self.numSolutions]:
                newPopulation.solutions.append(s)
        return newPopulation

    def run(self, numIterations):
        for i in range(numIterations):
            self.population = self.newPopulation()
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
