#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Binary Jaya example'''


import numpy as np
import math


# m: number of design variables
m = 21
# n: number of candidate solutions
n = 5
# i: number of iteration
number_iteration = 15


def funtion(solution):
    return sum(solution)


def generate_population(cant):
    '''cant: cantidad de soluciones a generar'''
    return np.random.randint(2, size=(cant, m)).astype(float)


def get_best_and_worst(population):
    for e, p in enumerate(population):
        if e == 0:
            best_item = worst_item = 0
            best_value = worst_value = funtion(p)
        else:
            value = funtion(p)
            if value < best_value:
                best_item = e
                best_value = value
            if value > worst_value:
                worst_item = e
                worst_value = value
    return {
        'best_item': best_item, 'best_value': best_value,
        'worst_item': worst_item, 'worst_value': worst_value}


def jaya():
    population = generate_population(n)
    result = get_best_and_worst(population)
    for i in range(number_iteration):
        population_aux = population.copy()
        for p in population_aux:
            r1 = np.random.rand(m)
            r2 = np.random.rand(m)
            for v_item, v_value in enumerate(p):
                p[v_item] = v_value+r1[v_item]*(population[result['best_item']][v_item]-abs(v_value))-r2[v_item]*(population[result['worst_item']][v_item]-abs(v_value))
                if np.random.rand() < math.tanh(abs(p[v_item])):
                    p[v_item] = 1.0
                else:
                    p[v_item] = 0.0
        for x in range(n):
            if funtion(population_aux[x]) < funtion(population[x]):
                population[x] = population_aux[x]
        result = get_best_and_worst(population)

    print(result)


def main():
    jaya()
    return 0


if __name__ == '__main__':
    main()
