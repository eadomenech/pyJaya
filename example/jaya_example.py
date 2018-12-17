#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Jaya example'''

import numpy as np


# m: number of design variables
m = 5
# n: number of candidate solutions
n = 5
# i: number of iteration
number_iteration = 4000


def funtion_to_minimize(solution):
    return sum(np.asarray(solution)**2)


def generate_population(cant):
    '''cant: cantidad de soluciones a generar'''
    return np.random.rand(cant, m)


def generate_population_static():
    p = np.random.rand(5, m)
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


def get_best_and_worst(population):
    for e, p in enumerate(population):
        if e == 0:
            best_item = worst_item = 0
            best_value = worst_value = funtion_to_minimize(p)
        else:
            value = funtion_to_minimize(p)
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
    # population = generate_population(n)
    population = generate_population_static()
    for i in range(number_iteration):
        result = get_best_and_worst(population)
        population_aux = population.copy()
        for p in population_aux:
            for v_item, v_value in enumerate(p):
                r1 = np.random.rand(m)
                r2 = np.random.rand(m)
                p[v_item] = v_value+r1[v_item]*(population[result['best_item']][v_item]-abs(v_value))-r2[v_item]*(population[result['worst_item']][v_item]-abs(v_value))
        for x in range(n):
            if funtion_to_minimize(population_aux[x]) < funtion_to_minimize(population[x]):
                population[x] = population_aux[x]
    result = get_best_and_worst(population)
    print result
    print(population[result['best_item']])


def main():
    jaya()
    return 0


if __name__ == '__main__':
    main()
