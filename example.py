# -*- coding: utf-8 -*-
from pyjaya.clasic import JayaClasic
from pyjaya.binary import JayaBinary
from pyjaya.selfAdadtive import JayaSelfAdadtive
from pyjaya.utils import FloatRange, IntRange, BinaryRange
import numpy as np


def function1(solution):
    return sum(np.asarray(solution)**2)


def function2(solution):
    return sum(solution)


def himmelblau(solution):
    return (solution[0]**2+solution[1]-11)**2+(solution[0]+solution[1]**2-7)**2


def himmelblauConstraintOne(solution):
    return (26-(solution[0]-5)**2-solution[1]**2) >= 0


def himmelblauConstraintTwo(solution):
    return (20-4*solution[0]-solution[1]) >= 0


def main():
    print("RUN: JayaClasic")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    jc = JayaClasic(5, listVars, function1)
    print(jc.run(100))
    print("--------------------------------------------------------------")

    print("RUN: JayaBinary")
    listVars = [BinaryRange() for i in range(10)]
    jc = JayaBinary(5, listVars, function2)
    jc.toMaximize()
    print(jc.run(100))
    print("--------------------------------------------------------------")

    print("RUN: JayaClasic")
    print("Minimize the Himmelblau constrained benchmark function.")
    listVars = [FloatRange(-5.0, 5.0) for i in range(2)]
    jc = JayaClasic(5, listVars, himmelblau)
    jc.addConstraint(himmelblauConstraintOne)
    jc.addConstraint(himmelblauConstraintTwo)
    print(jc.run(100))
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    print("Minimize the Himmelblau constrained benchmark function.")
    listVars = [FloatRange(-5.0, 5.0) for i in range(2)]
    jc = JayaSelfAdadtive(listVars, himmelblau)
    jc.addConstraint(himmelblauConstraintOne)
    jc.addConstraint(himmelblauConstraintTwo)
    print(jc.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
