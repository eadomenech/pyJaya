# -*- coding: utf-8 -*-
import numpy as np
import copy

from pyJaya.consts import minimaxType
from pyJaya.population import Population


class JayaBase(object):
    """Jaya base class

    Args:
        numSolutions (int): Number of solutions of population.
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        space (bool): Spaced numbers over a specified interval.
        minimaxType (minimaxType, optional): Min or Max. Defaults to [minimize]
        listConstraints (list, optional): Constraint list. Defaults to [].
        population (Population, optional): Population. Defaults to None.
    """

    def __init__(
            self, numSolutions, listVars, functionToEvaluate, space=False,
            minimaxType=minimaxType['minimize'], listConstraints=[],
            population=None):

        super(JayaBase, self).__init__()
        self.functionToEvaluate = functionToEvaluate
        self.numSolutions = numSolutions
        self.listVars = listVars
        self.cantVars = len(listVars)
        self.minimax = minimaxType
        self.listConstraints = listConstraints
        self.space = space

        if population is None:
            self.population = self.generatePopulation()
        else:
            self.population = copy.deepcopy(population)

    def generate_rn(self, number_iterations):
        """Generate random numbers
        """
        rn = [None] * number_iterations
        for iter in range(number_iterations):
            rn[iter] = [None] * self.cantVars
            for y in range(self.cantVars):
                rn[iter][y] = [None] * 2
                for j in range(2):
                    np.random.seed()
                    rn[iter][y][j] = np.random.rand()
        return rn

    def generatePopulation(self):
        """Generate population

        Returns:
            Population: Population generated.
        """
        population = Population(self.minimax)
        population.generate(
            self.numSolutions, self.listVars, self.functionToEvaluate,
            self.space, self.listConstraints)
        return population

    def addConstraint(self, constraintFuntion):
        """Add constraint

        Args:
            constraintFuntion (funtion): Funtion to add as constraint.
        """
        self.listConstraints.append(constraintFuntion)

    def toMaximize(self):
        """Change to maximize funtion.
        """
        self.minimax = minimaxType['maximize']
        self.population.toMaximize()

    def getBestAndWorst(self):
        """Best and worst value and solution

        Returns:
            dict: Best value, worst value, best solution and worst solution.
        """
        return self.population.getBestAndWorst()

    def run(self, number_iterations, rn=[]):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")
