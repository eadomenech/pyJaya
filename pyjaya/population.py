# -*- coding: utf-8 -*-
"""
Population class
"""
from .solution import Solution
from .consts import *
import numpy as np


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
        return sorted(self.solutions, key=lambda solution: solution.value)

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
