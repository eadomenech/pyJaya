# -*- coding: utf-8 -*-
from pyjaya.clasic import JayaClasic
from pyjaya.binary import JayaBinary
from pyjaya.selfAdadtive import JayaSelfAdadtive
from pyjaya.quasiOppositional import JayaQuasiOppositional
from pyjaya.samp import JayaSAMP
from pyjaya.sampe import JayaSAMPE
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
    ja = JayaClasic(20, listVars, function1)
    print(ja.run(1000))
    print("--------------------------------------------------------------")

    print("RUN: JayaBinary")
    listVars = [BinaryRange() for i in range(10)]
    ja = JayaBinary(5, listVars, function2)
    ja.toMaximize()
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("RUN: JayaClasic")
    print("Minimize the Himmelblau constrained benchmark function.")
    listVars = [FloatRange(-5.0, 5.0) for i in range(2)]
    ja = JayaClasic(20, listVars, himmelblau)
    ja.addConstraint(himmelblauConstraintOne)
    ja.addConstraint(himmelblauConstraintTwo)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    print("Minimize the Himmelblau constrained benchmark function.")
    listVars = [FloatRange(-5.0, 5.0) for i in range(2)]
    ja = JayaSelfAdadtive(listVars, himmelblau)
    ja.addConstraint(himmelblauConstraintOne)
    ja.addConstraint(himmelblauConstraintTwo)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    print("Minimize the Himmelblau constrained benchmark function.")
    listVars = [FloatRange(-5.0, 5.0) for i in range(2)]
    ja = JayaQuasiOppositional(20, listVars, himmelblau)
    ja.addConstraint(himmelblauConstraintOne)
    ja.addConstraint(himmelblauConstraintTwo)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSAMP(20, listVars, function1)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSAMPE(20, listVars, function1)
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
