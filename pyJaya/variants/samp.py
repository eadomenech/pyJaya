# -*- coding: utf-8 -*-
from .base import JayaBase
from pyJaya.population import Population
from pyJaya.solution import Solution
import numpy as np


class JayaSAMP(JayaBase):
    """Jaya SAMP class

    Args:
        numSolutions (int): Number of solutions of population.
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        listConstraints (list, optional): Constraint list. Defaults to [].
        population (Population, optional): Population. Defaults to None.
    """

    def sprint(self, population):
        """Jaya clasic to sub-population

        Args:
            population (Population): Population to evaluate whit Jaya clasic.

        Returns:
            Population: Sprint final population.
        """
        result = population.getBestAndWorst()
        r1 = np.random.rand(self.cantVars)
        r2 = np.random.rand(self.cantVars)
        for solution in population.solutions:
            solt = []
            for v_item, v_value in enumerate(solution.solution):
                solt.append(self.listVars[v_item].convert(
                    (
                        v_value+r1[v_item] *
                        (result['best_solution'][v_item] - abs(v_value)) -
                        r2[v_item] *
                        (result['worst_solution'][v_item]-abs(v_value)))
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
        return population

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
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        for i in range(number_iterations):
            if i == 0:
                m = 2
                subPopulations = self.population.divideInTo(m)
                for p in subPopulations:
                    p = self.sprint(p)
                newPopulation = Population(self.minimax, solutions=[])
                newPopulation.merge(subPopulations)
                if self.minimax:
                    nBest = newPopulation.getBestAndWorst()['best_value']
                    lBest = self.population.getBestAndWorst()['best_value']
                    if nBest > lBest:
                        self.population = newPopulation
                else:
                    nBest = newPopulation.getBestAndWorst()['best_value']
                    lBest = self.population.getBestAndWorst()['best_value']
                    if nBest < lBest:
                        self.population = newPopulation
            else:
                if self.minimax:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV > bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                    subPopulations = self.population.divideInTo(m)
                    for p in subPopulations:
                        p = self.sprint(p)
                    newPopulation = Population(self.minimax, solutions=[])
                    newPopulation.merge(subPopulations)
                    nBest = newPopulation.getBestAndWorst()['best_value']
                    lBest = self.population.getBestAndWorst()['best_value']
                    if nBest > lBest:
                        self.population = newPopulation
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                    subPopulations = self.population.divideInTo(m)
                    for p in subPopulations:
                        p = self.sprint(p)
                    newPopulation = Population(self.minimax, solutions=[])
                    newPopulation.merge(subPopulations)
                    newBest = newPopulation.getBestAndWorst()['best_value']
                    lastBest = self.population.getBestAndWorst()['best_value']
                    if newBest < lastBest:
                        self.population = newPopulation
        return self.population
