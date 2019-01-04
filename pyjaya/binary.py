# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
import numpy as np
import math


class JayaBinary(JayaBase):

    def run(self, number_iterations):
        result = self.population.getBestAndWorst()
        for i in range(number_iterations):
            r1 = np.random.rand(self.cantVars)
            r2 = np.random.rand(self.cantVars)
            newPopulation = Population(self.minimax)
            for solution in self.population.solutions:
                solt = []
                for v_item, v_value in enumerate(solution.solution):
                    v = v_value+r1[v_item] * (result['best_solution'][v_item] - abs(v_value)) - r2[v_item] * (result['worst_solution'][v_item]-abs(v_value))
                    if np.random.rand() > math.tanh(abs(v)):
                        solt.append(1.0)
                    else:
                        solt.append(0.0)
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
                newPopulation.solutions.append(solution)
                self.population = newPopulation

        return self.population.getBestAndWorst()

        # for i in range(number_iterations):
        #     population_aux = population.copy()
        #     for p in population_aux:
        #         r1 = np.random.rand(self.cantVars)
        #         r2 = np.random.rand(self.cantVars)
        #         for v_item, v_value in enumerate(p):
        #             p[v_item] = v_value+r1[v_item]*(population[result['best_item']][v_item]-abs(v_value))-r2[v_item]*(population[result['worst_item']][v_item]-abs(v_value))
        #             if np.random.rand() < math.tanh(abs(p[v_item])):
        #                 p[v_item] = 1.0
        #             else:
        #                 p[v_item] = 0.0
        #     for x in range(self.n):
        #         if self.minimax:
        #             if (
        #                     self.to_evaluate(population_aux[x]) >
        #                     self.to_evaluate(population[x])) and self.constraintsOK(population_aux[x]):
        #                 population[x] = population_aux[x]
        #         else:
        #             if (
        #                     self.to_evaluate(population_aux[x]) <
        #                     self.to_evaluate(population[x])) and self.constraintsOK(population_aux[x]):
        #                 population[x] = population_aux[x]
        # return self.getBestAndWorst(population)
