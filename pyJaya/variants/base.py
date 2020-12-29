# -*- coding: utf-8 -*-
from pyJaya.consts import minimaxType
from pyJaya.population import Population
import copy


class JayaBase(object):
    """Jaya base class

    Args:
        numSolutions (int): Number of solutions of population.
        listVars (list): Range list.
        functionToEvaluate (funtion): Function to minimize or maximize.
        listConstraints (list, optional): Constraint list. Defaults to [].
        population (Population, optional): Population. Defaults to None.
    """

    def __init__(
            self, numSolutions, listVars, functionToEvaluate,
            listConstraints=[], population=None):

        super(JayaBase, self).__init__()
        self.functionToEvaluate = functionToEvaluate
        self.numSolutions = numSolutions
        self.listVars = listVars
        self.cantVars = len(listVars)
        self.minimax = minimaxType['minimize']
        self.listConstraints = listConstraints

        if population is None:
            self.population = self.generatePopulation()
        else:
            self.population = copy.deepcopy(population)

    def generatePopulation(self):
        """Generate population

        Returns:
            Population: Population generated.
        """
        population = Population(self.minimax)
        population.generate(
            self.numSolutions, self.listVars, self.functionToEvaluate,
            self.listConstraints)
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

    def run(self, number_iterations):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")
