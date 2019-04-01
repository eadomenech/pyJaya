# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
import numpy as np


class JayaClasic(JayaBase):

    def run(self, number_iterations):
        for i in range(number_iterations):
            result = self.population.getBestAndWorst()

            np.random.seed()
            r1 = np.random.rand(self.cantVars)
            r2 = np.random.rand(self.cantVars)
            for solution in self.population.solutions:
                solt = []
                for v_item, v_value in enumerate(solution.solution):
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
