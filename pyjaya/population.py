# -*- coding: utf-8 -*-
"""
Population class
"""
from pyjaya.solution import Solution
from pyjaya.consts import *
import numpy as np
import copy


class Population():

    def __init__(self, minimax):
        self.solutions = []
        self.minimax = minimax

    def generate(
            self, numSolutions, listVars, functionToEvaluate,
            listConstraints):
        for i in range(numSolutions):
            solution = Solution(
                listVars, functionToEvaluate, listConstraints)
            solution.generate()
            self.solutions.append(solution)

    def toMaximize(self):
        self.minimax = minimaxType['maximize']

    def sorted(self):
        return sorted(
            self.solutions, reverse=self.minimax,
            key=lambda solution: solution.value)

    def getBestAndWorst(self):
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
        listSolutions = []
        for p in listPopulation:
            listSolutions += p.solutions
        self.solutions = sorted(
            listSolutions, reverse=self.minimax,
            key=lambda solution: solution.value)
    
    def size(self):
        return len(self.solutions)
