# -*- coding: utf-8 -*-
from .consts import *
import numpy as np


class JayaBase(object):

    def __init__(
            self, num_solutions, listVars, function_to_evaluate):
        super(JayaBase, self).__init__()
        self.to_evaluate = function_to_evaluate
        self.n = num_solutions
        self.listVars = listVars
        self.cantVars = len(listVars)
        self.minimax = minimaxType['minimize']

    def generatePopulation(self):
        p = np.zeros([self.n, self.cantVars])
        for row_index, row_value in enumerate(p):
            for column_item, column_value in enumerate(row_value):
                p[row_index, column_item] = self.listVars[column_item].get()
        return p

    def toMaximize(self):
        self.minimax = minimaxType['maximize']

    def getBestAndWorst(self, population):
        for e, p in enumerate(population):
            if e == 0:
                best_item = worst_item = 0
                best_value = worst_value = self.to_evaluate(*[p])
            else:
                value = self.to_evaluate(*[p])
                if self.minimax:
                    if value > best_value:
                        best_item = e
                        best_value = value
                    if value < worst_value:
                        worst_item = e
                        worst_value = value
                else:
                    if value < best_value:
                        best_item = e
                        best_value = value
                    if value > worst_value:
                        worst_item = e
                        worst_value = value
        return {
            'best_item': best_item, 'best_value': best_value,
            'worst_item': worst_item, 'worst_value': worst_value,
            'best_solution': population[best_item],
            'worst_solution': population[best_item]}

    def run(self, number_iterations):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")
