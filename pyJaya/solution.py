# -*- coding: utf-8 -*-
"""
Solution class
"""
import numpy as np


class Solution():
    """Solution class

    Args:
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        listConstraints (list, optional): Constraint list. Defaults to [].
    """

    def __repr__(self):
        """Represent

        Returns:
            str: Solution represent.
        """
        return self.__str__()

    def __str__(self):
        """Str

        Returns:
            str: Solution represent.
        """
        return str(self.solution)

    def __init__(
            self, listVars, functionToEvaluate, listConstraints=[]):

        self.cantVars = len(listVars)
        self.listVars = listVars
        self.listConstraints = listConstraints
        self.functionToEvaluate = functionToEvaluate

        self.solution = np.zeros(self.cantVars)
        self.value = None

    def generate(self):
        """Generate a solution"""

        while True:
            solution = np.zeros(self.cantVars)
            for item in range(self.cantVars):
                solution[item] = self.listVars[item].get()
            if self.constraintsOK(solution):
                self.solution = solution
                break
        self.value = self.evaluate()

    def constraintsOK(self, solution):
        """Check that the solution satisfies the constraints

        Args:
            solution (Solution): Solution to check.

        Returns:
            Bool: True if it satisfies the constraints, False if not.
        """
        for constraints in self.listConstraints:
            if not constraints(*[solution]):
                return False
        return True

    def evaluate(self):
        """Evaluate the solution

        Returns:
            Float: Result when evaluating the solution.
        """
        return self.functionToEvaluate(tuple(*[self.solution]))

    def setSolution(self, solution):
        """Set solution

        Args:
            solution (list or np.array): Solution to be assigned.
        """
        self.solution = solution
        self.value = self.evaluate()
