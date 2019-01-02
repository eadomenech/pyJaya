# -*- coding: utf-8 -*-
"""
Population class
"""
from .solution import Solution
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
        # listValores = []
        # for solution in self.sorted():
        #     listValores.append(solution.value)
        # for e, p in enumerate(population):
        #     if e == 0:
        #         best_item = worst_item = 0
        #         best_value = worst_value = self.to_evaluate(*[p])
        #     else:
        #         value = self.to_evaluate(*[p])
        #         if self.minimax:
        #             if value > best_value:
        #                 best_item = e
        #                 best_value = value
        #             if value < worst_value:
        #                 worst_item = e
        #                 worst_value = value
        #         else:
        #             if value < best_value:
        #                 best_item = e
        #                 best_value = value
        #             if value > worst_value:
        #                 worst_item = e
        #                 worst_value = value
        # return {
        #     'best_item': best_item, 'best_value': best_value,
        #     'worst_item': worst_item, 'worst_value': worst_value,
        #     'best_solution': population[best_item],
        #     'worst_solution': population[best_item]}
