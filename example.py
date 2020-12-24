# -*- coding: utf-8 -*-
from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.binary import JayaBinary
from pyJaya.variants.selfAdadtive import JayaSelfAdadtive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
# from pyJaya.sampe import JayaSAMPE
from pyJaya.variants.sampemultiprocess import JayaSAMPE
from pyJaya.utils import FloatRange, IntRange, BinaryRange
import numpy as np


def sumOfSquares(solution):
    return sum(np.asarray(solution)**2)


def suma(solution):
    return sum(solution)


def himmelblau(solution):
    return (solution[0]**2+solution[1]-11)**2+(solution[0]+solution[1]**2-7)**2


def himmelblauConstraintOne(solution):
    return (26-(solution[0]-5)**2-solution[1]**2) >= 0


def himmelblauConstraintTwo(solution):
    return (20-4*solution[0]-solution[1]) >= 0


def main():
    print("Minimizing sum of squares using float numbers")
    print("RUN: JayaClasic")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaClasic(20, listVars, sumOfSquares)
    print(ja.run(200).getBestAndWorst())
    print("--------------------------------------------------------------")
    
    print("Maximizing sum of binary numbers")
    print("RUN: JayaBinary")
    listVars = [BinaryRange() for i in range(10)]
    ja = JayaBinary(20, listVars, suma)
    ja.toMaximize()
    print(ja.run(200).getBestAndWorst())
    print("--------------------------------------------------------------")
    
    print("Minimizing sum of squares using float numbers")
    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSelfAdadtive(listVars, sumOfSquares)
    print(ja.run(200).getBestAndWorst())
    print("--------------------------------------------------------------")
    
    print("Minimizing sum of squares using float numbers")
    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaQuasiOppositional(20, listVars, sumOfSquares)
    print(ja.run(200).getBestAndWorst())
    print("--------------------------------------------------------------")
    
    print("Minimizing sum of squares using float numbers")
    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSAMP(20, listVars, sumOfSquares)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print("Minimizing sum of squares using float numbers")
    print("RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya Algorithm MultiProcess")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSAMPE(20, listVars, sumOfSquares)
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
