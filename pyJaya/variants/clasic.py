# -*- coding: utf-8 -*-
import numpy as np

from pyJaya.variants.base import JayaBase
from pyJaya.solution import Solution


class JayaClasic(JayaBase):
    """Jaya clasic class

    Args:
        numSolutions (int): Number of solutions of population.
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        space (bool): Spaced numbers over a specified interval.
        minimaxType (minimaxType, optional): Min or Max. Defaults to [minimize]
        listConstraints (list, optional): Constraint list. Defaults to [].
        population (Population, optional): Population. Defaults to None.
    """

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
        for i in range(number_iterations):
            result = self.population.getBestAndWorst()
            for solution in self.population.solutions:
                solt = []
                for v_item, v_value in enumerate(solution.solution):
                    solt.append(self.listVars[v_item].convert(
                        (
                            v_value + self.rn[i][v_item][0] *
                            (result['best_solution'][v_item] - abs(v_value))
                            - self.rn[i][v_item][1] *
                            (result['worst_solution'][v_item]-abs(v_value)))
                    ))
                auxSolution = Solution(
                    self.listVars, self.functionToEvaluate,
                    self.listConstraints)
                auxSolution.setSolution(np.array(solt))
                if self.minimax:
                    if (auxSolution.value > solution.value) and \
                            (auxSolution.constraintsOK(np.array(solt))):
                        solution.setSolution(auxSolution.solution)
                else:
                    if (auxSolution.value < solution.value) and \
                            (auxSolution.constraintsOK(np.array(solt))):
                        solution.setSolution(auxSolution.solution)

        return self.population
