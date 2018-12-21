# -*- coding: utf-8 -*-
from .consts import *


class JayaBase(object):

    def __init__(
            self, num_solutions, num_variables, function_to_evaluate):
        super(JayaBase, self).__init__()
        self.to_evaluate = function_to_evaluate
        self.n = num_solutions
        self.m = num_variables
        self.minimax = minimaxType['minimize']

    def generatePopulation(self):
        """Clients must implement this method and call the parent method"""
        raise NotImplementedError()

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
            'worst_item': worst_item, 'worst_value': worst_value}

    def run(self, number_iterations):
        """Cada metodo debe implementarlo"""
        raise NotImplementedError(
            "Client must define it self")
