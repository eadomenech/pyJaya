# -*- coding: utf-8 -*-
from .base import JayaBase
from .population import Population
from .solution import Solution
import numpy as np
import queue
import threading

q = queue.Queue()
num_worker_threads = 2


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        js, popu = item
        js.sprint(popu)
        q.task_done()


threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)


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

    def run(self, number_iterations):
        result = self.population.getBestAndWorst()
        bestValue = result['best_value']
        for i in range(number_iterations):
            if i == 0:
                m = 2
                subPopulations = self.population.divideInToWithElitist(m)
                for p in subPopulations:
                    q.put((self, p))
                    # p = self.sprint(p)
                q.join()
                newPopulation = Population(self.minimax)
                newPopulation.merge(subPopulations)
                if self.minimax:
                    if newPopulation.getBestAndWorst()['best_value'] > self.population.getBestAndWorst()['best_value']:
                        self.population = newPopulation
                else:
                    if newPopulation.getBestAndWorst()['best_value'] < self.population.getBestAndWorst()['best_value']:
                        self.population = newPopulation
            else:
                if self.minimax:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV > bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                    subPopulations = self.population.divideInToWithElitist(m)
                    for p in subPopulations:
                        q.put((self, p))
                        # p = self.sprint(p)
                    q.join()
                    newPopulation = Population(self.minimax)
                    newPopulation.merge(subPopulations)
                    if newPopulation.getBestAndWorst()['best_value'] > self.population.getBestAndWorst()['best_value']:
                        self.population = newPopulation
                else:
                    bV = self.population.getBestAndWorst()['best_value']
                    if bV < bestValue:
                        if m < self.numSolutions:
                            m += 1
                        bestValue = bV
                    elif m > 1:
                        m -= 1
                    subPopulations = self.population.divideInToWithElitist(m)
                    for p in subPopulations:
                        q.put((self, p))
                        # p = self.sprint(p)
                    q.join()
                    newPopulation = Population(self.minimax)
                    newPopulation.merge(subPopulations)
                    if newPopulation.getBestAndWorst()['best_value'] < self.population.getBestAndWorst()['best_value']:
                        self.population = newPopulation
        for i in range(num_worker_threads):
            q.put(None)
        for t in threads:
            t.join()

        return self.population.getBestAndWorst()
