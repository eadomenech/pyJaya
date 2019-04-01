# -*- coding: utf-8 -*-
from .consts import *
import numpy as np
from .population import Population


class JayaBase(object):

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

        self.population = self.generatePopulation()
        # if population is None:
        #     self.population = self.generatePopulation()
        # else:
        #     self.population = population

    def generatePopulation(self):
        population = Population(self.minimax)
        population.generate(
            self.numSolutions, self.listVars, self.functionToEvaluate,
            self.listConstraints)
        return population

    def addConstraint(self, constraintFuntion):
        self.listConstraints.append(constraintFuntion)

    def toMaximize(self):
        self.minimax = minimaxType['maximize']
        self.population.toMaximize()

    def run(self, number_iterations):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")
