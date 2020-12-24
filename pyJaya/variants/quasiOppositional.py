# -*- coding: utf-8 -*-
from .base import JayaBase
from .clasic import JayaClasic
from pyJaya.population import Population
from pyJaya.solution import Solution
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
            self.population = JayaClasic(
                self.population.size(), self.listVars,
                self.functionToEvaluate, self.listConstraints,
                self.population).run(1)

        return self.population
