# -*- coding: utf-8 -*-
"""
Population class
"""
import copy
import random

import numpy as np

from pyJaya.solution import Solution
from pyJaya.consts import minimaxType


class Population():
    """Population class

    Args:
        minimax (int): Objective function to be (0: minimized or 1: maximized).
    """

    def __init__(self, minimax, solutions=[]):
        """Population init"""
        self.solutions = solutions
        self.minimax = minimax

    def generate(
            self, numSolutions, listVars, functionToEvaluate, space,
            listConstraints):
        """Population generator

        Args:
            numSolutions (int): Number of solutions.
            listVars (list): Range list.
            functionToEvaluate (funtion): Function to minimize or maximize.
            space (bool): Spaced numbers over a specified interval.
            listConstraints (list, optional): Constraint list. Defaults to [].
        """
        if space:
            v = []
            for item in listVars:
                l = np.linspace(item.minor, item.major, numSolutions).tolist()
                random.shuffle(l)
                v.append(l)
            for i in range(numSolutions):
                solution = Solution(
                    listVars, functionToEvaluate, listConstraints)
                s = []
                for item, value in enumerate(listVars):
                    s.append(value.convert(v[item][i]))
                solution.setSolution(s)
                self.solutions.append(solution)
        else:
            for i in range(numSolutions):
                solution = Solution(
                    listVars, functionToEvaluate, listConstraints)
                solution.generate()
                self.solutions.append(solution)

    def toMaximize(self):
        """Switch to maximize function
        """
        self.minimax = minimaxType['maximize']

    def sorted(self):
        """Sort the solutions

        Returns:
            list: List sorted solutions.
        """
        return sorted(
            self.solutions, reverse=self.minimax,
            key=lambda solution: solution.value)

    def getBestAndWorst(self):
        """Best and worst value and solution

        Returns:
            dict: Best value, worst value, best solution and worst solution.
        """
        solutionSorted = self.sorted()
        if self.minimax:
            return {
                'best_value': solutionSorted[-1].value,
                'worst_value': solutionSorted[0].value,
                'best_solution': solutionSorted[-1].solution,
                'worst_solution': solutionSorted[0].solution}
        else:
            return {
                'best_value': solutionSorted[0].value,
                'worst_value': solutionSorted[-1].value,
                'best_solution': solutionSorted[0].solution,
                'worst_solution': solutionSorted[-1].solution}

    def divideInTo(self, n=2):
        """Divide the population into n subpopulations

        Args:
            n (int, optional): Number of subpopulations. Defaults to 2.

        Returns:
            list: Subpopulations list.
        """
        if n == 1:
            return [self]
        populations = []
        q, r = divmod(len(self.solutions), n)
        indices = [q*i + min(i, r) for i in range(n+1)]
        subLists = [self.sorted()[indices[i]:indices[i+1]] for i in range(n)]
        for miniList in subLists:
            newPopulation = Population(self.minimax)
            newPopulation.solutions = miniList
            populations.append(newPopulation)
        return populations

    def divideInToWithElitist(self, n=2):
        """Divide the population into n subpopulations with elitism

        Args:
            n (int, optional): Number of subpopulations. Defaults to 2.

        Returns:
            list: Subpopulations list.
        """
        if n == 1:
            return [self]
        populations = []
        q, r = divmod(len(self.solutions), n)
        indices = [q*i + min(i, r) for i in range(n+1)]
        subLists = [self.sorted()[indices[i]:indices[i+1]] for i in range(n)]
        for miniList in subLists[:-1]:
            newPopulation = Population(self.minimax)
            newPopulation.solutions = miniList
            populations.append(newPopulation)
        newPopulation = Population(self.minimax)
        newPopulation.solutions = copy.deepcopy(populations[0].solutions)
        populations.append(newPopulation)
        return populations

    def merge(self, listPopulation):
        """Merge subpopulations and sort your solutions

        Args:
            listPopulation (list): Population list.
        """
        listSolutions = []
        for p in listPopulation:
            listSolutions += p.solutions
        self.solutions = sorted(
            listSolutions, reverse=self.minimax,
            key=lambda solution: solution.value)

    def size(self):
        """Get population size

        Returns:
            int: Number of solutions in the population.
        """
        return len(self.solutions)
