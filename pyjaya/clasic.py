# -*- coding: utf-8 -*-
from .core import JayaBase
import numpy as np


class JayaClasic(JayaBase):

    def generatePopulation(self):
        p = np.random.rand(5, self.m)
        p[0, 0] = -5.0
        p[0, 1] = 18.0
        p[1, 0] = 14.0
        p[1, 1] = 63.0
        p[2, 0] = 70.0
        p[2, 1] = -6.0
        p[3, 0] = -8.0
        p[3, 1] = 7
        p[4, 0] = -12
        p[4, 1] = -18
        return p

    def run(self, number_iterations):
        population = self.generatePopulation()
        for i in range(number_iterations):
            result = self.getBestAndWorst(population)
            population_aux = population.copy()
            for p in population_aux:
                for v_item, v_value in enumerate(p):
                    r1 = np.random.rand(self.m)
                    r2 = np.random.rand(self.m)
                    p[v_item] = (v_value+r1[v_item] * (population[result['best_item']][v_item] - abs(v_value))- r2[v_item]* (population[result['worst_item']][v_item]-abs(v_value)))
            for x in range(self.n):
                if self.minimax:
                    if (
                            self.to_evaluate(population_aux[x]) >
                            self.to_evaluate(population[x])):
                        population[x] = population_aux[x]
                else:
                    if (
                            self.to_evaluate(population_aux[x]) <
                            self.to_evaluate(population[x])):
                        population[x] = population_aux[x]

        return self.getBestAndWorst(population)
