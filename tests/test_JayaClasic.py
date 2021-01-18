"""Tests for Jaya Clasic variant."""

import numpy as np
import math

from pyJaya.solution import Solution
from pyJaya.population import Population
from pyJaya.variants.clasic import JayaClasic
from pyJaya.variables import VariableFloat


def sphere(solution):
    return sum(np.asarray(solution)**2)


def rastrigin(solution):
    f = 0.0
    for x in solution:
        f += x ** 2 - 10 * math.cos(2 * math.pi * x) + 10
    return f


def himmelblau(solution):
    return (
        solution[0] ** 2 + solution[1] - 11) ** 2 +\
        (solution[0] + solution[1] ** 2 - 7) ** 2


def himmelblauConstraintOne(solution):
    return (26 - (solution[0] - 5) ** 2 - solution[1] ** 2) >= 0


def himmelblauConstraintTwo(solution):
    return (20 - 4 * solution[0] - solution[1]) >= 0


def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class TestUnconstrainedJayaClasicInSphere:
    """Unconstrained Jaya Clasic in Sphere tests"""

    def setup(self):
        # scaling factors
        self.index = 0
        self.rn = [0.58, 0.81, 0.92, 0.49, 0.27, 0.23, 0.38, 0.51]
        # Solutions
        s1 = Solution([], sphere)
        s1.setSolution(np.array([-5.0, 18.0]))
        s2 = Solution([], sphere)
        s2.setSolution(np.array([14.0, 63.0]))
        s3 = Solution([], sphere)
        s3.setSolution(np.array([70.0, -6.0]))
        s4 = Solution([], sphere)
        s4.setSolution(np.array([-8.0, 7.0]))
        s5 = Solution([], sphere)
        s5.setSolution(np.array([-12.0, -18.0]))
        # Population
        self.population = Population(0, solutions=[s1, s2, s3, s4, s5])

    def test_first_iteration(self, monkeypatch):
        """Tests first iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-100.0, 100.0) for i in range(2)]
        ja = JayaClasic(5, listVars, sphere, population=self.population)
        bw = ja.run(1).getBestAndWorst()
        assert bw['best_value'] == 113.0
        assert len(bw['best_solution']) == 2
        assert all([a == b for a, b in zip(bw['best_solution'], [-8.0, 7.0])])
        assert truncate(bw['worst_value'], 1) == 3997.7
        assert len(bw['worst_solution']) == 2
        assert all(
            [a == b for a, b in zip(bw['worst_solution'], [-44.12, 45.29])])

    def test_second_iteration(self, monkeypatch):
        """Tests second iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-100.0, 100.0) for i in range(2)]
        ja = JayaClasic(5, listVars, sphere, population=self.population)
        bw = ja.run(2).getBestAndWorst()
        assert truncate(bw['best_value'], 2) == 7.78
        assert len(bw['best_solution']) == 2
        assert truncate(bw['best_solution'][0], 3) == 2.787
        assert truncate(bw['best_solution'][1], 3) == -0.097
        assert truncate(bw['worst_value'], 2) == 2381.13
        assert len(bw['worst_solution']) == 2
        assert truncate(bw['worst_solution'][0], 3) == -37.897
        assert truncate(bw['worst_solution'][1], 3) == 30.739


class TestUnconstrainedJayaClasicInRastringin:
    """Unconstrained Jaya Clasic in Rastringin tests"""

    def setup(self):
        self.index = 0
        # scaling factors
        self.rn = [
            0.38, 0.81, 0.92, 0.49, 0.65, 0.23,
            0.38, 0.51, 0.01, 0.7, 0.02, 0.5]
        # Solutions
        s1 = Solution([], rastrigin)
        s1.setSolution(np.array([-4.570261872, 0.045197073]))
        s2 = Solution([], rastrigin)
        s2.setSolution(np.array([3.574220009, 1.823157605]))
        s3 = Solution([], rastrigin)
        s3.setSolution(np.array([-2.304524513, 4.442417134]))
        s4 = Solution([], rastrigin)
        s4.setSolution(np.array([-1.062187325, -0.767182961]))
        s5 = Solution([], rastrigin)
        s5.setSolution(np.array([-0.84373426, 3.348170112]))
        # Population
        self.population = Population(0, solutions=[s1, s2, s3, s4, s5])

    def test_first_iteration(self, monkeypatch):
        """Tests first iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-5.12, 5.12) for i in range(2)]
        ja = JayaClasic(5, listVars, rastrigin, population=self.population)
        bw = ja.run(1).getBestAndWorst()
        assert truncate(bw['best_value'], 9) == 2.108371360
        assert len(bw['best_solution']) == 2
        assert truncate(bw['best_solution'][0], 9) == 0.982105143
        assert truncate(bw['best_solution'][1], 9) == -0.974135755
        assert truncate(bw['worst_value'], 9) == 36.785779376
        assert len(bw['worst_solution']) == 2
        assert truncate(bw['worst_solution'][0], 2) == 5.12
        assert truncate(bw['worst_solution'][1], 11) == -1.84339288493

    def test_second_iteration(self, monkeypatch):
        """Tests second iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-5.12, 5.12) for i in range(2)]
        ja = JayaClasic(5, listVars, rastrigin, population=self.population)
        bw = ja.run(2).getBestAndWorst()
        assert truncate(bw['best_value'], 9) == 2.108371360
        assert len(bw['best_solution']) == 2
        assert truncate(bw['best_solution'][0], 9) == 0.982105143
        assert truncate(bw['best_solution'][1], 9) == -0.974135755
        assert truncate(bw['worst_value'], 8) == 26.25808866
        assert len(bw['worst_solution']) == 2
        assert truncate(bw['worst_solution'][0], 10) == 2.4303683434
        assert truncate(bw['worst_solution'][1], 10) == -1.0337930258

    def test_third_iteration(self, monkeypatch):
        """Tests third iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-5.12, 5.12) for i in range(2)]
        ja = JayaClasic(5, listVars, rastrigin, population=self.population)
        bw = ja.run(3).getBestAndWorst()
        assert truncate(bw['best_value'], 7) == 0.2150036
        assert len(bw['best_solution']) == 2
        assert truncate(bw['best_solution'][0], 9) == -0.031679095
        assert truncate(bw['best_solution'][1], 10) == -0.0091367952
        assert truncate(bw['worst_value'], 8) == 24.79038297
        assert len(bw['worst_solution']) == 2
        assert truncate(bw['worst_solution'][0], 9) == 2.415885711
        assert truncate(bw['worst_solution'][1], 9) == -0.040158575


class TestConstrainedJayaClasicInHimmelblau:
    """Constrained Jaya Clasic in Himmelblau tests"""

    def setup(self):
        self.index = 0
        # scaling factors
        self.rn = [0.25, 0.43, 0.47, 0.33]
        # Solutions
        s1 = Solution([], himmelblau)
        s1.setSolution(np.array([3.22, 0.403]))
        s2 = Solution([], himmelblau)
        s2.setSolution(np.array([0.191, 2.289]))
        s3 = Solution([], himmelblau)
        s3.setSolution(np.array([3.182, 0.335]))
        s4 = Solution([], himmelblau)
        s4.setSolution(np.array([1.66, 4.593]))
        s5 = Solution([], himmelblau)
        s5.setSolution(np.array([2.214, 0.867]))
        # Population
        self.population = Population(0, solutions=[s1, s2, s3, s4, s5])

    def test_first_iteration(self, monkeypatch):
        """Tests first iteration."""

        def rn():
            self.index += 1
            return self.rn[self.index-1]
        monkeypatch.setattr(np.random, 'rand', rn)

        listVars = [VariableFloat(-5.0, 5.0) for i in range(2)]
        ja = JayaClasic(
            5, listVars, himmelblau, population=self.population,
            listConstraints=[
                himmelblauConstraintOne,
                himmelblauConstraintTwo])
        bw = ja.run(1).getBestAndWorst()
        assert truncate(bw['best_value'], 3) == 11.890
        assert len(bw['best_solution']) == 2
        assert truncate(bw['best_solution'][0], 3) == 3.845
        assert truncate(bw['best_solution'][1], 3) == -1.038
        assert truncate(bw['worst_value'], 3) == 77.710
        assert len(bw['worst_solution']) == 2
        assert truncate(bw['worst_solution'][0], 3) == 0.191
        assert truncate(bw['worst_solution'][1], 3) == 2.289
