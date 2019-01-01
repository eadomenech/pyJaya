# -*- coding: utf-8 -*-
from .base import JayaBase
import numpy as np


class JayaClasic(JayaBase):

    def run(self, number_iterations):
        population = self.generatePopulation()
        for i in range(number_iterations):
            result = self.getBestAndWorst(population)
            population_aux = population.copy()
            for p in population_aux:
                for v_item, v_value in enumerate(p):
                    r1 = np.random.rand(self.cantVars)
                    r2 = np.random.rand(self.cantVars)
                    p[v_item] = self.listVars[v_item].convert(
                        (v_value+r1[v_item] * (population[result['best_item']][v_item] - abs(v_value))- r2[v_item]* (population[result['worst_item']][v_item]-abs(v_value)))
                    )
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
