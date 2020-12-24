# -*- coding: utf-8 -*-
"""
Solution class
"""
import numpy as np


class Solution():

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.solution)

    def __init__(self, listVars, functionToEvaluate, listConstraints=[]):

        self.cantVars = len(listVars)
        self.listVars = listVars
        self.listConstraints = listConstraints
        self.functionToEvaluate = functionToEvaluate

        self.solution = np.zeros(self.cantVars)
        self.value = None

    def generate(self):
        while 1:
            solution = np.zeros(self.cantVars)
            for item in range(self.cantVars):
                solution[item] = self.listVars[item].get()
            if self.constraintsOK(solution):
                self.solution = solution
                break
        self.value = self.evaluate()
        # print("solution.generate:", self.solution)

    def constraintsOK(self, solution):
        for constraints in self.listConstraints:
            if not constraints(*[solution]):
                return False
        return True

    def evaluate(self):
        return self.functionToEvaluate(*[self.solution])

    def setSolution(self, solution):
        self.solution = solution
        self.value = self.evaluate()
