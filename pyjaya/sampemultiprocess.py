# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
from multiprocessing import Process, Queue, current_process, freeze_support
import numpy as np


class JayaSAMPE(JayaBase):

    def sprint(self, population):
        result = population.getBestAndWorst()
        r1 = np.random.rand(self.cantVars)
        r2 = np.random.rand(self.cantVars)
        for solution in population.solutions:
            solt = []
            for v_item, v_value in enumerate(solution.solution):
                solt.append(self.listVars[v_item].convert(
                    (v_value+r1[v_item] * (result['best_solution'][v_item] - abs(v_value)) - r2[v_item] * (result['worst_solution'][v_item]-abs(v_value)))
                ))
            auxSolution = Solution(
                self.listVars, self.functionToEvaluate,
                self.listConstraints)
            auxSolution.setSolution(np.array(solt))
            if self.minimax:
                if (auxSolution.value > solution.value) and \
                        (auxSolution.constraintsOK(np.array(solt))):
                    solution = auxSolution
            else:
                if (auxSolution.value < solution.value) and \
                        (auxSolution.constraintsOK(np.array(solt))):
                    solution.setSolution(auxSolution.solution)
        return population

    @staticmethod
    def worker(input, output):
        for sampe, population in iter(input.get, 'STOP'):
            result = sampe.sprint(population)
            output.put(result)

    def generate(self, m):
        NUMBER_OF_PROCESSES = m

        input_queue = Queue()
        output_queue = Queue()

        subPopulations = list()
        TASKS = [(self, p) for p in self.population.divideInToWithElitist(m)]
        [input_queue.put(e) for e in TASKS]

        for i in range(NUMBER_OF_PROCESSES):
            Process(
                target=JayaSAMPE.worker, args=(
                    input_queue, output_queue)).start()

        # Get results of sprint
        for i in range(len(TASKS)):
            subPopulations.append(output_queue.get())

        # Tell child processes to stop
        for i in range(NUMBER_OF_PROCESSES):
            input_queue.put('STOP')

        newPopulation = Population(self.minimax)
        newPopulation.merge(subPopulations)
        new_best_value = newPopulation.getBestAndWorst()['best_value']
        old_best_value = self.population.getBestAndWorst()['best_value']

        if self.minimax:
            if new_best_value > old_best_value:
                self.population = newPopulation
        else:
            if new_best_value < old_best_value:
                self.population = newPopulation

    def run(self, number_iterations):
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        m = 2
        for i in range(number_iterations):
            if i == 0:
                self.generate(2)
            else:
                if self.minimax:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV > bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                self.generate(m)
        return self.population.getBestAndWorst()
