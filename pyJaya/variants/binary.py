# -*- coding: utf-8 -*-
from .base import JayaBase
from pyJaya.population import Solution
import numpy as np
import math


class JayaBinary(JayaBase):
    """Jaya binary class

    Args:
        numSolutions (int): Number of solutions of population.
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        listConstraints (list, optional): Constraint list. Defaults to [].
        population (Population, optional): Population. Defaults to None.
    """

    def run(self, number_iterations):
        """Run method

        Args:
            number_iterations (int): Number of iterations.

        Returns:
            Population: Final population.
        """
        for i in range(number_iterations):
            result = self.population.getBestAndWorst()
            np.random.seed()
            r1 = np.random.rand(self.cantVars)
            r2 = np.random.rand(self.cantVars)
            for solution in self.population.solutions:
                solt = []
                for v_item, v_value in enumerate(solution.solution):
                    v = v_value + r1[v_item] *\
                        (result['best_solution'][v_item] - abs(v_value)) -\
                        r2[v_item] *\
                        (result['worst_solution'][v_item]-abs(v_value))
                    if math.tanh(abs(v)) > 0.5:
                        solt.append(1.0)
                    else:
                        solt.append(0.0)
                auxSolution = Solution(
                    self.listVars, self.functionToEvaluate,
                    self.listConstraints)
                auxSolution.setSolution(np.asarray(solt))
                if self.minimax:
                    if (auxSolution.value > solution.value) and \
                            (auxSolution.constraintsOK(np.asarray(solt))):
                        solution.setSolution(auxSolution.solution)
                else:
                    if (auxSolution.value < solution.value) and \
                            (auxSolution.constraintsOK(np.asarray(solt))):
                        solution.setSolution(auxSolution.solution)

        return self.population
