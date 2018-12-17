# -*- coding: utf-8 -*-
from .core import JayaBase
import numpy as np
import math


class JayaBinary(JayaBase):

    def generatePopulation(self):
        return np.random.randint(2, size=(self.n, self.m)).astype(float)

    def run(self, number_iterations):
        population = self.generatePopulation()
        result = self.getBestAndWorst(population)
        for i in range(number_iterations):
            population_aux = population.copy()
            for p in population_aux:
                r1 = np.random.rand(self.m)
                r2 = np.random.rand(self.m)
                for v_item, v_value in enumerate(p):
                    p[v_item] = v_value+r1[v_item]*(population[result['best_item']][v_item]-abs(v_value))-r2[v_item]*(population[result['worst_item']][v_item]-abs(v_value))
                    if np.random.rand() < math.tanh(abs(p[v_item])):
                        p[v_item] = 1.0
                    else:
                        p[v_item] = 0.0
            for x in range(self.n):
                if (
                        self.to_evaluate(population_aux[x]) <
                        self.to_evaluate(population[x])):
                    population[x] = population_aux[x]
        return self.getBestAndWorst(population)
