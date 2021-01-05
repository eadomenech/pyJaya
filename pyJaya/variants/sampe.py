# -*- coding: utf-8 -*-
from multiprocessing import Pool

import numpy as np

from .base import JayaBase
from .clasic import JayaClasic
from pyJaya.population import Population
from pyJaya.solution import Solution


class JayaSAMPE(JayaBase):
    """Jaya SAMPE class

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

    def run(self, number_iterations):
        """Run method

        Args:
            number_iterations (int): Number of iterations.

        Returns:
            Population: Final population.
        """
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        for i in range(number_iterations):
            if i == 0:
                m = 2
                subPopulations = self.population.divideInToWithElitist(m)
                for p in subPopulations:
                    p = self.sprint(p)
                newPopulation = Population(self.minimax)
                newPopulation.merge(subPopulations)
                if self.minimax:
                    newBest = newPopulation.getBestAndWorst()['best_value']
                    lastBest = self.population.getBestAndWorst()['best_value']
                    if newBest > lastBest:
                        self.population = newPopulation
                else:
                    newBest = newPopulation.getBestAndWorst()['best_value']
                    lastBest = self.population.getBestAndWorst()['best_value']
                    if newBest < lastBest:
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
                    subPopulations = self.population.divideInToWithElitist(m)
                    for p in subPopulations:
                        p = self.sprint(p)
                    newPopulation = Population(self.minimax)
                    newPopulation.merge(subPopulations)
                    newBest = newPopulation.getBestAndWorst()['best_value']
                    lastBest = self.population.getBestAndWorst()['best_value']
                    if newBest > lastBest:
                        self.population = newPopulation
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                    subPopulations = self.population.divideInToWithElitist(m)
                    for p in subPopulations:
                        p = self.sprint(p)
                    newPopulation = Population(self.minimax)
                    newPopulation.merge(subPopulations)
                    newBest = newPopulation.getBestAndWorst()['best_value']
                    lastBest = self.population.getBestAndWorst()['best_value']
                    if newBest < lastBest:
                        self.population = newPopulation
        return self.population


class MultiprocessJayaSAMPE(JayaBase):
    """Multiprocess Jaya SAMPE class

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

        numSolutions = len(population.solutions)
        jaya_clasic = JayaClasic(
            numSolutions, self.listVars, self.functionToEvaluate,
            population=population)
        if self.minimax:
            jaya_clasic.toMaximize()

        population = jaya_clasic.run(1)
        return population

    @staticmethod
    def worker(sampe, population):
        """Worker method

        Args:
            population (Population): Original population.

        Returns:
            Population: Generated population by sprint.
        """
        return sampe.sprint(population)

    def generate(self, m):
        """Generate population

        Args:
            m (int): Number of groups based on the quality of the solutions.

        Returns:
            Population: Generated population.
        """
        entrada = self.population.divideInToWithElitist(m)
        pool = Pool(processes=3)
        results = [
            pool.apply_async(
                MultiprocessJayaSAMPE.worker,
                args=(self, x)) for x in entrada]
        subPopulations = [p.get() for p in results]

        newPopulation = Population(self.minimax)
        newPopulation.merge(subPopulations)
        self.population = newPopulation

    def run(self, number_iterations):
        """Run method

        Args:
            number_iterations (int): Number of iterations.

        Returns:
            Population: Final population.
        """
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        m = 2
        for i in range(number_iterations):
            if i == 0:
                self.generate(2)
            else:
                if self.minimax:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV > bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 2:
                        m -= 1
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m <= self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 2:
                        m -= 1
                self.generate(m)
        return self.population
