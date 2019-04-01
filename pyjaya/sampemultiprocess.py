# -*- coding: utf-8 -*-
from .base import JayaBase
from pyjaya.clasic import JayaClasic
from .population import Population
from .solution import Solution
from multiprocessing import Process, Queue, current_process, freeze_support
from multiprocessing import Pool
import numpy as np


class JayaSAMPE(JayaBase):

    def sprint(self, population):
        result = population.getBestAndWorst()
        solutions = list()

        numSolutions = len(population.solutions)
        jaya_intance = JayaClasic(
            numSolutions, self.listVars, self.functionToEvaluate,
            population=population)
        if self.minimax:
            jaya_intance.toMaximize()
        jaya_intance.run(1)

        # np.random.seed()
        # r1 = np.random.rand(self.cantVars)
        # r2 = np.random.rand(self.cantVars)
        #
        # for solution in population.solutions:
        #     solt = []
        #     for v_item, v_value in enumerate(solution.solution):
        #         solt.append(self.listVars[v_item].convert(
        #             (v_value+r1[v_item] * (result['best_solution'][v_item] - abs(v_value)) - r2[v_item] * (result['worst_solution'][v_item]-abs(v_value)))
        #         ))
        #     auxSolution = Solution(
        #         self.listVars, self.functionToEvaluate,
        #         self.listConstraints)
        #     auxSolution.setSolution(np.array(solt))
        #     if self.minimax:
        #         if (auxSolution.value > solution.value) and \
        #                 (auxSolution.constraintsOK(np.array(solt))):
        #             solutions.append(auxSolution)
        #         else:
        #             solutions.append(solution)
        #     else:
        #         if (auxSolution.value < solution.value) and \
        #                 (auxSolution.constraintsOK(np.array(solt))):
        #             solutions.append(auxSolution)
        #         else:
        #             solutions.append(solution)
        # newPop = Population(self.minimax)
        # newPop.solutions = solutions
        # print("sprint", solutions)
        # return newPop
        print("worker", jaya_intance.population.solutions)
        return jaya_intance.population

    @staticmethod
    def worker(sampe, population):
        return sampe.sprint(population)

    def generate(self, m):
        entrada = self.population.divideInToWithElitist(m)
        print("     ### entradas")
        [print(e.solutions) for e in entrada]
        print("     ###")
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
        print("Clasic", self.population.solutions)

    def run(self, number_iterations):
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        m = 2
        for i in range(number_iterations):
            print(i, self.population.solutions)
            if i == 0:
                print("Generaring 2")
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
                print("Generaring", m)
                self.generate(m)
                print("done", m)
        return self.population.getBestAndWorst()
