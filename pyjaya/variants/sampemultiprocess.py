# -*- coding: utf-8 -*-
from .base import JayaBase
from .clasic import JayaClasic
from pyjaya.population import Population
from pyjaya.solution import Solution
from multiprocessing import Process, Queue, current_process, freeze_support
from multiprocessing import Pool
import numpy as np


class JayaSAMPE(JayaBase):

    def sprint(self, population):
        # result = population.getBestAndWorst()
        # solutions = list()

        numSolutions = len(population.solutions)
        jaya_clasic = JayaClasic(
            numSolutions, self.listVars, self.functionToEvaluate,
            population=population)
        if self.minimax:
            jaya_clasic.toMaximize()

        population = jaya_clasic.run(1)
        return population

    @staticmethod
    def worker(sampe, population):
        return sampe.sprint(population)

    def generate(self, m):
        entrada = self.population.divideInToWithElitist(m)
        # print("     ### entradas (luego de la division con elitismo)")
        # [print(e.solutions) for e in entrada]
        # print("     ###")
        pool = Pool(processes=3)
        results = [
            pool.apply_async(
                JayaSAMPE.worker, args=(self, x)) for x in entrada]
        subPopulations = [p.get() for p in results]

        newPopulation = Population(self.minimax)
        newPopulation.merge(subPopulations)
        # new_best_value = newPopulation.getBestAndWorst()['best_value']
        # old_best_value = self.population.getBestAndWorst()['best_value']
        #
        # if self.minimax:
        #     if new_best_value > old_best_value:
        #         self.population = newPopulation
        # else:
        #     if new_best_value < old_best_value:
        #         self.population = newPopulation
        #         self.population = newPopulation
        # newPopulation.getBestAndWorst()
        self.population = newPopulation

    def run(self, number_iterations):
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        m = 2
        for i in range(number_iterations):
            # print(i, self.population.solutions)
            if i == 0:
                # print("Generaring", m)
                self.generate(2)
            else:
                if self.minimax:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV > bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 2:
                        m -= 1
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m <= self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 2:
                        m -= 1
                # print("Generaring", m)
                self.generate(m)
                # print("done", m)
        return self.population.getBestAndWorst()
